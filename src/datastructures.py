
"""
update this file to implement the following already declared methods:
- add_member: Should add a member to the self._members list
- delete_member: Should delete a member from the self._members list
- update_member: Should update a member from the self._members list
- get_member: Should return a member from the self._members list
"""
from random import randint

class FamilyStructure:
    def __init__(self, last_name):
        self.last_name = last_name

        # example list of members
        self._members = [
            {'name': 'John Jackson',
              'age': 33,
              'lucky_numbers': [7,11,33],
              'id': 1     
            },
            {'name': 'Jane Jackson',
              'age': 35,
              'lucky_numbers': [8,1,10],
              'id': 2      
            },
            {'name': 'Jimmy Jackson',
              'age': 5,
              'lucky_numbers': [5,6,9],
              'id': 3     
            }
        ]

    # read-only: Use this method to generate random members ID's when adding members into the list
    def _generateId(self):
        return randint(0, 99999999)

    def add_member(self, new_member):
        # fill this method and update the return
        id_to_add = self._generateId()
        duplicate = filter(lambda member: id_to_add == member["id"], self._members)
        if not duplicate:
            return add_member(member)
        else:
            new_member['id'] = id_to_add
            self._members.append(new_member)
            return self._members

    def delete_member(self, id):
        # fill this method and update the return
        result = list(filter(lambda member: member['id'] != id, self._members))
        if len(result) == len(self._members):
            return False
        else:
            return True




    def get_member(self, id):
        # fill this method and update the return
        for x in self._members:
            if x['id'] == id:
                member = x
        return member
   
    # this method is done, it returns a list with all the family members
    def get_all_members(self):
        return self._members
