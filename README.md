## Simple Virtual Coffee challenge
# Context


Think-it is an international engineering collective dedicated to developing technology solutions to help teams and our planet do more with less. As part of our engagement, we want to support and empower Think-iteers to meet regularly for chats despite the physical distance to share ideas once in a while.

The challenge we faced was how to make it easy for an international team to find common time slots for what we call "virtual coffee chats". To tackle this challenge and make it easier to find mutual dates, we need your help.

# Target solution
Functional requirements
We want to provide Think-iteers with a software system that allows them to easily find other Thinkiteers who are available for virtual coffee chats. For the scope of this exercise, we look at a 1-day scale. The input to such a system is described with 1 line for each participant described as follow:

The Thinkiteer’s name
The Thinkiteer's timezone (offset to GMT, more on that later)
The Thinkiteer's availability (start and end of the availability slot) for the day
name timezone_offset slot_1_start-slot_1_end ... slot_n_start-slot_n_end
The software system will then fetch the desired number of participants from the standard input and computes common slots for a virtual coffee chat. If no common slots exist, the program should return an empty string.

Note: we only consider 1-hour slots when computing common slots. For example, if my availability is from 8am to 11am and the other Thinkiteer is available from 9am to 3pm, then we have 2 common slots of 1-hour. First slot is from 9am to 10am and second slot is from 10am to 11am.

# Assume that:
timezone_offset is following the GMT format "+X" or "-Y" where X and Y are the offset.
slot_n_start-slot_n_end are integers within the range [0..23];


# Example:
Input

Amin +2 9-13 14-18

May +8 9-10 11-13 20-23

Karl -5 8-18

Output
13-14 14-15
