from mamba import *
from expects import *
from day7.device import Shell, Filesystem, LogProcessor


with description('Day 7'):
    with description('With a filesystem'):
        with before.all as self:
            fs = Filesystem(disk_size=70000000)
            self.shell = Shell(filesystem=fs)
        with context('when command is cd /'):
            with it('current working directory is / (top)'):
                self.shell.cd('/')
                expect(self.shell.cwd.name).to(equal('/'))
                expect(self.shell.cwd.parent).to(be_none)
        with context('when adding a file with name b.txt and size 14848514'):
            with context('/ directory'):
                with it('must have one child'):
                    self.shell.add_file(14848514, 'b.txt')
                    expect(len(self.shell.filesystem.root.childs)).to(equal(1))
                with it('must be sized as 14848514'):
                    expect(self.shell.filesystem.root.size).to(equal(14848514))
        with context('when adding a file with name c.dat and size 8504156'):
            with context('/ directory'):
                with it('must have two child'):
                    self.shell.add_file(8504156, 'c.dat')
                    expect(len(self.shell.filesystem.root.childs)).to(equal(2))
                with it('must be sized as 14848514 + 8504156'):
                    expect(self.shell.filesystem.root.size).to(equal(14848514 + 8504156))
        
        with context('when command is cd a'):
            with it('current working directory is a'):
                self.shell.cd('a')
                expect(self.shell.cwd.name).to(equal('a'))
            with it('parent directory should be /'):
                expect(self.shell.cwd.parent.name).to(equal('/'))
        
        with context('when adding files 29116 f, 2557 g, 62596 h.lst'):
            with context('a directory'):
                with it('must have the child'):
                    self.shell.add_files([(29116, 'f'), (2557, 'g'), (62596, 'h.lst')])
                    expect(len(self.shell.filesystem.cwd.childs)).to(equal(3))
                with it('must be sized as 29116 + 2557 + 62596'):
                    expect(self.shell.filesystem.cwd.size).to(equal(29116 + 2557 + 62596))
        
        with context('when command is cd e'):
            with it('current working directory is e'):
                self.shell.cd('e')
                expect(self.shell.cwd.name).to(equal('e'))
            with it('parent directory should be a'):
                expect(self.shell.cwd.parent.name).to(equal('a'))
        
        with context('when adding a file with name i and size 584'):
            with context('e directory'):
                with it('must have one child'):
                    self.shell.add_file(584, 'i')
                    expect(len(self.shell.filesystem.cwd.childs)).to(equal(1))
                with it('must be sized as 584'):
                    expect(self.shell.filesystem.cwd.size).to(equal(584))
        
        with context('when command is cd ..'):
            with it('current working directory is a'):
                self.shell.cd('..')
                expect(self.shell.cwd.name).to(equal('a'))
            with it('parent directory should be /'):
                expect(self.shell.cwd.parent.name).to(equal('/'))
        
        with context('when command is cd ..'):
            with it('current working directory is /'):
                self.shell.cd('..')
                expect(self.shell.cwd.name).to(equal('/'))
            with it('parent directory should be none'):
                expect(self.shell.cwd.parent).to(be_none)
        
        with context('when command is cd d'):
            with it('current working directory is d'):
                self.shell.cd('d')
                expect(self.shell.cwd.name).to(equal('d'))
            with it('parent directory should be /'):
                expect(self.shell.cwd.parent.name).to(equal('/'))
        
        with context('when adding files 4060174 j, 8033020 d.log, 5626152 d.ext, 7214296 k'):
            with context('d directory'):
                with it('must have 4 childs'):
                    self.shell.add_files([(4060174, 'j'), (8033020, 'd.log'), (5626152, 'd.ext'), (7214296, 'k')])
                    expect(len(self.shell.filesystem.cwd.childs)).to(equal(4))
                with it('must be sized as 4060174 + 8033020 + 5626152 + 7214296'):
                    expect(self.shell.filesystem.cwd.size).to(equal(4060174 + 8033020 + 5626152 + 7214296))
        
        with description('Calculating directory sizes'):
            with context('Getting /a/e directory'):
                with before.all as self:
                    self.d = self.shell.filesystem.get_path('/a/e')
                with it('should be e directory'):
                    expect(self.d.name).to(equal('e'))
                with it('should be size of 584'):
                    expect(self.d.size).to(equal(584))
            
            with context('Getting /a directory'):
                with before.all as self:
                    self.d = self.shell.filesystem.get_path('/a')
                with it('should be a directory'):
                    expect(self.d.name).to(equal('a'))
                with it('should be size of 94853'):
                    expect(self.d.size).to(equal(94853))
            
            with context('Getting /d directory'):
                with before.all as self:
                    self.d = self.shell.filesystem.get_path('/d')
                with it('should be d directory'):
                    expect(self.d.name).to(equal('d'))
                with it('should be size of 24933642'):
                    expect(self.d.size).to(equal(24933642))
            
            with context('Getting / directory'):
                with before.all as self:
                    self.d = self.shell.filesystem.get_path('/')
                with it('should be / directory'):
                    expect(self.d.name).to(equal('/'))
                with it('should be size of 48381165'):
                    expect(self.d.size).to(equal(48381165))
            
            with it('should be 21618835 as free space'):
                expect(self.shell.filesystem.free).to(equal(21618835))
        
        with description('Getting at most 100000 directories'):
            with it('should be a and e directories and sum of 95437'):
                dirs = self.shell.filesystem.get_at_most()
                expect([d.name for d in dirs]).to(contain_only('a', 'e'))
                expect(sum(d.size for d in dirs)).to(equal(95437))
        
        with description('Getting the minimal directory'):
            with it('should be d directory with size 24933642'):
                update_space = 30000000
                free = self.shell.filesystem.free
                need_space_for = update_space - free
                dirs = self.shell.filesystem.get_at_min(need_space_for)
                min_dir = sorted(dirs, key=lambda x: x.size, reverse=True)[0]
                expect(min_dir.name).to(equal('d'))
                expect(min_dir.size).to(equal(24933642))
                    

    with description('Parsing a log console'):
        with before.all as self:
            fs = Filesystem()
            shell = Shell(fs)

            input = """
            $ cd /
            $ ls
            dir a
            14848514 b.txt
            8504156 c.dat
            dir d
            $ cd a
            $ ls
            dir e
            29116 f
            2557 g
            62596 h.lst
            $ cd e
            $ ls
            584 i
            $ cd ..
            $ cd ..
            $ cd d
            $ ls
            4060174 j
            8033020 d.log
            5626152 d.ext
            7214296 k
            """

            self.log = LogProcessor(input, shell)
        
        with description('Getting at most 100000 directories'):
            with it('should be a and e directories and sum of 95437'):
                dirs = self.log.shell.filesystem.get_at_most()
                expect([d.name for d in dirs]).to(contain_only('a', 'e'))
                expect(sum(d.size for d in dirs)).to(equal(95437))