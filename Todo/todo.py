from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.orm import sessionmaker
from datetime import datetime, timedelta


class ToDo:
    Base = declarative_base()

    class Table(Base):
        """The database model of a task"""
        # noinspection SpellCheckingInspection
        __tablename__ = 'task'
        id = Column(Integer, primary_key=True)
        task = Column(String, default='Unnamed task')
        deadline = Column(Date, default=datetime.today())

        def __repr__(self):
            return f'{self.id}. {self.task}'

    def __init__(self):
        self.session = None
        self.menu_choice = ''
        self.init_database()

    def init_database(self):
        """Creates and initializes a database"""
        engine = create_engine('sqlite:///todo.db?check_same_thread=False')
        self.Base.metadata.create_all(engine)
        self.session = sessionmaker(bind=engine)()

    def menu(self):
        """Prints menu items and accepts user choice"""
        print('1) Today\'s tasks')
        print('2) Week\'s tasks')
        print('3) All tasks')
        print('4) Missed tasks')
        print('5) Add task')
        print('6) Delete task')
        print('0) Exit')
        self.menu_choice = input()

    def show_today_tasks(self):
        """Outputs all tasks for today"""
        today = datetime.today()
        tasks = self.session.query(self.Table).filter(self.Table.deadline == today.strftime('%Y-%m-%d')).all()
        print(f'Today {today.strftime("%d %b")}:')
        if tasks:
            for n, task in enumerate(tasks, 1):
                print(f'{n}. {task.task}')
        else:
            print('Nothing to do!')
        print()

    def show_weeks_tasks(self):
        """Outputs all tasks for next seven days"""
        for day in [datetime.today() + timedelta(days=i) for i in range(7)]:
            tasks = self.session.query(self.Table).filter(self.Table.deadline == day.strftime('%Y-%m-%d')).\
                order_by(self.Table.deadline).all()
            print(f'{day.strftime("%A")} {day.strftime("%d %b")}:')
            if tasks:
                for n, task in enumerate(tasks, 1):
                    print(f'{n}. {task.task}')
            else:
                print('Nothing to do!')
            print()

    def show_all_tasks(self):
        """Shows all tasks from the database"""
        tasks = self.session.query(self.Table).order_by(self.Table.deadline).all()
        print('All tasks:')
        if tasks:
            for n, task in enumerate(tasks, 1):
                print(f'{n}. {task.task}. {task.deadline.strftime("%d %b")}')
        else:
            print('Nothing to do!')
        print()

    def show_missed_tasks(self):
        """Shows all missed tasks from the database"""
        tasks = self.session.query(self.Table).filter(self.Table.deadline < datetime.today().strftime('%Y-%m-%d')).\
            order_by(self.Table.deadline).all()
        print('Missed tasks:')
        if tasks:
            for n, task in enumerate(tasks, 1):
                print(f'{n}. {task.task}. {task.deadline.strftime("%d %b")}')
        else:
            print('Nothing is missed!')
        print()

    def add_task(self):
        """Add a task to the database"""
        print('Enter task')
        text_task = input()
        print('Enter deadline')
        new_task = self.Table(task=text_task, deadline=datetime.strptime(input(), '%Y-%m-%d'))
        self.session.add(new_task)
        self.session.commit()
        print('The task has been added!')
        print()

    def delete_task(self):
        """Delete a chosen task from the database"""
        tasks = self.session.query(self.Table).order_by(self.Table.deadline).all()
        if tasks:
            print('Chose the number of the task you want to delete:')
            for n, task in enumerate(tasks, 1):
                print(f'{n}. {task.task}. {task.deadline.strftime("%d %b")}')
            self.session.query(self.Table).filter(self.Table.id == tasks[int(input())-1].id).delete()
            self.session.commit()
        else:
            print('Nothing to delete!')
        print()

    def run(self):
        """Main logic of the program"""
        while True:
            self.menu()
            if self.menu_choice == '1':
                self.show_today_tasks()
            elif self.menu_choice == '2':
                self.show_weeks_tasks()
            elif self.menu_choice == '3':
                self.show_all_tasks()
            elif self.menu_choice == '4':
                self.show_missed_tasks()
            elif self.menu_choice == '5':
                self.add_task()
            elif self.menu_choice == '6':
                self.delete_task()
            else:
                print('Bye!')
                break


if __name__ == '__main__':
    todo = ToDo()
    todo.run()