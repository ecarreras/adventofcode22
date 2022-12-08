class File:
    def __init__(self, name, size, parent):
        self.parent = parent
        self.name = name
        self.size = size


class Directory:
    def __init__(self, name, parent=None):
        self.parent = parent
        self.childs = {}
        self.name = name
    
    @property
    def size(self):
        return sum(i.size for i in self.childs.values())
    
    @property
    def child_directories(self):
        return [d for d in self.childs.values() if isinstance(d, Directory)]
    
    def get_max_size(self, size):
        return self.get_size(size, 'max')
    
    def get_min_size(self, size):
        return self.get_size(size, 'min')
    
    def get_size(self, size, mode='max'):
        dirs = []
        
        for d in self.child_directories:
            if mode == 'max' and d.size <= size:
                dirs.append(d)
            elif mode == 'min' and d.size >= size:
                dirs.append(d)
            dirs += d.get_size(size, mode)
        return dirs


class Filesystem:
    def __init__(self, root: Directory = None, disk_size = None) -> None:
        if root is None:
            root = Directory('/')
        self.root = root
        self.cwd = root
        self.disk_size = disk_size
    
    def add(self, item):
        if item.name not in self.cwd.childs:
            self.cwd.childs[item.name] = item
    
    @property
    def free(self):
        return self.disk_size - self.root.size
    
    def get_path(self, path):
        dirs = path.split('/')
        if dirs[0] == '':
            d = self.root
        else:
            d = self.cwd
        for p in dirs:
            if p:
                d = d.childs.get(p)
        return d
    
    def get_at_most(self, size=100000):
        return self.root.get_max_size(size)
    
    def get_at_min(self, size):
        return self.root.get_min_size(size)
        

class Shell:
    def __init__(self, filesystem: Filesystem) -> None:
        self.filesystem = filesystem
    
    @property
    def cwd(self):
        return self.filesystem.cwd
    
    def cd(self, directory: str):
        if directory == self.filesystem.root.name:
            self.filesystem.cwd = self.filesystem.root
        elif directory == "..":
            self.filesystem.cwd = self.filesystem.cwd.parent
        else:
            d = Directory(directory, parent=self.cwd)
            self.filesystem.add(d)
            self.filesystem.cwd = d
        
    
    def add_file(self, size, name):
        f = File(name, size, parent=self.cwd)
        self.filesystem.add(f)
    
    def add_files(self, files):
        for size, name in files:
            self.add_file(size, name)


class LogProcessor:
    def __init__(self, input, shell):
        self.shell = shell
        files = []
        for line in input.strip().split('\n'):
            args = line.split()
            if args[0] == '$':
                if args[1] == 'cd':
                    self.shell.cd(args[2])
                elif args[1] == 'ls':
                    files = []
            elif args[0] == 'dir':
                continue
            else:
                self.shell.add_file(int(args[0]), args[1])
