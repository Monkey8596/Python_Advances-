from Data_filtrer import DATA

def run():
    # all_python_devs= [ worker ['name'] for worker in DATA if worker ['language'] == 'python' ]
    all_python_devs = list(filter(lambda worker: worker ['language'] == 'python', DATA ))

    # all_platzi_workers = [worker ['name'] for worker in DATA if worker ['organization'] == 'Platzi' ]
    all_platzi_workers = list(map(lambda worker: worker ['organization'] == 'Platzi', DATA  ))

    # adults = list(filter(lambda worker: worker['age'] > 18 , DATA))
    adults = [worker for worker in DATA if worker['age'] > 18]

    # adults=list(map(lambda worker: worker ['name'], adults))
    adults = [worker['name'] for worker in adults ]

    # old_people = list(map(lambda worker: worker | {'old': worker['age'] > 70}, DATA ))
    old_people = [worker for worker in DATA if worker['age'] > 70 ]
    # old_people = list(map(lambda worker: {**worker, **{"old": worker["age"] > 70}}, DATA))




    # for worker in all_python_devs:
    #     print(worker)

    # for worker in all_platzi_workers:
    #     print(worker)

    # for worker in adults:
    #     print( worker)
    
    # for worker in old_people:
    #     print(worker)

    for worker in all_python_devs, all_platzi_workers, adults, old_people:
        print(worker)






if __name__ == '__main__':
    run()