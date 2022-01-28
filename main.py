import json
import os

class App():
    def __init__(self, *args):
        self.items = []
        self.deleted_items = []

        self.highest_id = 0
        self.item_text = ""
        self.item_id = ""

    def start(self):
        self.read_data()

        print("st -- Show Todos | at -- Add Todo | ct -- Complete Task | dct -- Delete Completed Tasks")
        self.answer = input('\n> ')

        self.get_highest_id()

        if self.answer == 'st':
            self.show_todo()
        elif self.answer == 'at':
            self.get_user_input()
        elif self.answer == 'ct':
            self.complete_task()
        elif self.answer == 'dct':
            self.delete_complete_task()
        else: 
            print("Sorry something went wrong...")
            print("Try again...")
            self.start()


    def read_data(self):
        with open('data.json', 'r') as f:
            self.items = json.load(f)
           
    def write_data(self):
        with open('data.json', 'w') as f:
            json.dump(self.items, f)
        
        self.start()

    def get_highest_id(self):
        self.highest_id = self.items['items'][-1]['id'] + 1
        
    def add_item(self, item_text):
        self.item_text = ""
        self.item_id = ""

        self.data = {'id': self.highest_id, 'text': item_text, 'complete': False};

        self.items['items'].append(self.data)

        self.write_data()

        self.get_user_input()

    def get_user_input(self):
        print('- Input task name -')
        self.item_text = input('> ')

        while self.item_text != '':
            self.get_highest_id()
            self.add_item(self.item_text)
        else: 
            self.start()

    def show_todo(self):
        print('\n-------------------------')
        print('--------- Todos ---------')
        print('-------------------------\n')
        for todo in self.items['items']:
            if todo['complete'] == False:
                print('[+]', todo['text'])
            else: 
                print('[-]', todo['text'])
        print('\n-------------------------')
        print('-------------------------\n')
        
        self.start()

    def complete_task(self):
        print('\n--------- Todos ---------')
        print('-------------------------\n')
        for todo in self.items['items']:
            if todo['complete'] == False:
                print('[Not Completed]', "[{}]".format(todo['id']), todo['text'])
            else: 
                print('[Completed]', "[{}]".format(todo['id']), todo['text'])
        print('\n-------------------------')
        print('-------------------------\n')

        print('Which task do you want to mark as complete?')
        self.answer_int = input('\n> ')


        for todo in self.items['items']:
            if str(todo['id']) == self.answer_int:
                todo['complete'] = True
            
        while self.answer_int != '':
            self.complete_task()
            
        else: 
            self.write_data()

    def delete(self):
        for i in self.item['items']:
            self.delete_complete_task()
        
        self.write_data()

    def delete_complete_task(self):
        # pass
        for item in self.items['items']:
            if str(item['complete']) == str(True):
                print("Found Item to Delete")
                self.items['items'].pop(self.items['items'].index(item))



app = App()
app.start()