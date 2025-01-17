from pm4py.objects.log.importer.xes import importer as xes_importer
import sys
log = xes_importer.apply('Pl_2020_role.xes')

for case_index, case in enumerate(log):
    event_list=list(enumerate(case))
    old_event_index = -1
    for event_index, event in enumerate(case):
        if event["concept:name"] == "S":
            for i in range(1,event_index):
                prev_index = event_index-i
                complete_event = event_list[prev_index]
                catchedEvent = complete_event[1]
                if catchedEvent["concept:name"].startswith("2_"):
                    if prev_index == old_event_index:
                        break
                    old_event_index=prev_index
                    file = open('trigger_text.csv', 'a')
                    sys.stdout = file
                    print(case.attributes["concept:name"], ",",catchedEvent["time:timestamp"], ",",catchedEvent["concept:name"])
                    print(case.attributes["concept:name"], ",",event["time:timestamp"], ",",event["concept:name"])
                    break
                    file.close()
counter_list = list(enumerate(log))




