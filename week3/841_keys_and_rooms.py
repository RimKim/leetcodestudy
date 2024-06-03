# https://leetcode.com/problems/keys-and-rooms/
from typing import List


def can_visit_all_rooms(rooms: List[List[int]]) -> bool:
    room_keys = {r: k for r, k in enumerate(rooms)}
    visited_rooms = set()

    def open_room(room):
        if room in visited_rooms:
            return
        visited_rooms.add(room)
        for key in room_keys[room]:
            open_room(key)

    open_room(0)
    return len(visited_rooms) == len(rooms)
