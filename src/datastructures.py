
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
            {'id': self._generateId(),
             'first_name': 'John',
             'last_name': last_name,   
             'age': 33,
             'lucky_numbers': [7,13,22],    
            },
            {'id': self._generateId(),
             'first_name': 'Jane',
             'last_name': last_name,
              'age': 35,
              'lucky_numbers': [10,14,3],     
            },
            {'id': self._generateId(),
             'first_name': 'Jimmy',
             'last_name': last_name,
              'age': 5,
              'lucky_numbers': [1],    
            }
        ]

    # read-only: Use this method to generate random members ID's when adding members into the list
    def _generateId(self):
        return randint(0, 99999999)

    def add_member(self, new_member):
        # fill this method and update the return
        duplicate = filter(lambda member: member['id'] == member["id"], self._members)
        if not duplicate:
            new_member['id'] = self._generateId()     
        self._members.append(new_member)
        return self._members

    def delete_member(self, id):
        # fill this method and update the return
        result = list(filter(lambda member: member['id'] != id, self._members))
        if len(result) == len(self._members):
            raise APIException('ID not found',400)
        else:
            member_to_delete = self.get_member(id)
            self._members.remove(member_to_delete)
            
            return {'done': True}

    def get_member(self, id):
        # fill this method and update the return
        for x in self._members:
            if x['id'] == id:
                member = x
                return member
        return False
    # this method is done, it returns a list with all the family members
    def get_all_members(self):
        return self._members
