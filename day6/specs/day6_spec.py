from mamba import *
from expects import *
from day6.device import Decoder


with description('Day 6'):
    with description('Decoding a message'):
        with context('whe message is mjqjpqmgbljsphdztnvjfqwrcgsmlb'):
            with it('should be 7 the position'):
                d = Decoder('mjqjpqmgbljsphdztnvjfqwrcgsmlb')
                expect(d.find_first_marker()).to(equal(7))

        with context('when message is bvwbjplbgvbhsrlpgdmjqwftvncz'):
            with it('should be 5 the position'):
                d = Decoder('bvwbjplbgvbhsrlpgdmjqwftvncz')
                expect(d.find_first_marker()).to(equal(5))

        with context('when message is nppdvjthqldpwncqszvftbrmjlhg'):
            with it('should be 6 the position'):
                d = Decoder('nppdvjthqldpwncqszvftbrmjlhg')
                expect(d.find_first_marker()).to(equal(6))

        with context('when message is nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg'):
            with it('should be 10 the position'):
                d = Decoder('nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg')
                expect(d.find_first_marker()).to(equal(10))
        
        with context('when message is zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw'):
            with it('should be 11 the position'):
                d = Decoder('zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw')
                expect(d.find_first_marker()).to(equal(11))

    with description('Decoding a message with 14 packet length'):
        with context('whe message is mjqjpqmgbljsphdztnvjfqwrcgsmlb'):
            with it('should be 19 the position'):
                d = Decoder('mjqjpqmgbljsphdztnvjfqwrcgsmlb', packet_length=14)
                expect(d.find_first_marker()).to(equal(19))

        with context('when message is bvwbjplbgvbhsrlpgdmjqwftvncz'):
            with it('should be 23 the position'):
                d = Decoder('bvwbjplbgvbhsrlpgdmjqwftvncz', packet_length=14)
                expect(d.find_first_marker()).to(equal(23))

        with context('when message is nppdvjthqldpwncqszvftbrmjlhg'):
            with it('should be 23 the position'):
                d = Decoder('nppdvjthqldpwncqszvftbrmjlhg', packet_length=14)
                expect(d.find_first_marker()).to(equal(23))

        with context('when message is nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg'):
            with it('should be 29 the position'):
                d = Decoder('nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg', packet_length=14)
                expect(d.find_first_marker()).to(equal(29))
        
        with context('when message is zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw'):
            with it('should be 26 the position'):
                d = Decoder('zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw', packet_length=14)
                expect(d.find_first_marker()).to(equal(26))