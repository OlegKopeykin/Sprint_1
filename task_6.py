import copy


types = {
    1: 'Блокирующий',
    2: 'Критический',
    3: 'Значительный',
    4: 'Незначительный',
    5: 'Тривиальный'
}

tickets = {
    1: ['API_45', 'API_76', 'E2E_4'],
    2: ['UI_19', 'API_65', 'API_76', 'E2E_45'],
    3: ['E2E_45', 'API_45', 'E2E_2'],
    4: ['E2E_9', 'API_76'],
    5: ['E2E_2', 'API_61']
}


def remove_duplicate_tickets(tickets):
    copy_tickets = copy.deepcopy(tickets)
    all_tickets = []
    duplicate_tickets = {}
    for ticket in tickets.values():
        all_tickets += ticket
    for ticket in all_tickets:
        duplicate_tickets[ticket] = duplicate_tickets.get(ticket, 0) + 1

    for key, values in copy_tickets.items():
        for ticket in values:
            ticket_count = duplicate_tickets.get(ticket, 0)
            if ticket_count > 1:
                for idx in range(1, 6):
                    if idx <= key:
                        continue
                    if ticket in tickets[idx]:
                        tickets[idx].remove(ticket)
                        duplicate_tickets[ticket] -= 1

    return tickets

def create_tickets_by_type(tickets, types):
    dict_tickets = {}
    for new_list in range(1, len(tickets) + 1):
        dict_tickets[types[new_list]] = tickets[new_list]
    return dict_tickets

remove_duplicate_tickets(tickets)
tickets_by_type = create_tickets_by_type(tickets, types)
print(tickets_by_type)