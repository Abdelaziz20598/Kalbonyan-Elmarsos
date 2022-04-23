class Attendee:

    def __init__(self, name, tickets):
        self.name = name
        self.tickets = tickets

    def displayAttendee(self):
        print('Name : {}, Tickets: {}'.format(self.name, self.tickets))

    def addTickets(self):
        self.tickets += 1
        print('{} tickets increased to {}'.format(self.name, self.tickets))

attendee1 = Attendee('Omar', 1)
attendee2 = Attendee("Amr", 2)

attendee1.displayAttendee()
attendee2.displayAttendee()

attendee1.addTickets()
attendee1.displayAttendee()
attendee2.displayAttendee()