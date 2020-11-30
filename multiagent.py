#Работа магазина по продаже Iphone
#Seller -продавец, у него есть список устройств
#Customer - покупатель, ищет телефон
#Seller спрашивает у Customer модель телефона и стоимость

import json
from pade.acl.messages import ACLMessage
from pade.misc.utility import display_message, start_loop
from pade.core.agent import Agent
from pade.acl.aid import AID
from sys import argv
import random

smartphone = [["Iphone 12 pro","128 gb"],["Iphone 12 pro ","256 gb"],["Iphone se","256 gb"],["Iphone 11","128 gb"],
              ["Iphone 11","256 gb],["Iphone 11","512 gb"],["Iphone 11 pro,"256 gb"],["Iphone 8,"64 gb"]]

costs = [[90000],[99000],[50000],[89000],[95000],[106000],[96000],[35990]]

class Customer(Agent):
    def __init__(self, aid):
        super(Customer, self).__init__(aid=aid, debug=False)
        self.get_knowledge()
        self.timesAsked = 0;

    def get_knowledge(self):
        num = random.randint(0,len(smartphone)-1)
        self.knowledge = smartfone[num][0:len(smartphone[num])]
        self.knowledge2 = costs[num][0]

    def on_start(self):
        super().on_start()
        self.call_later(10, self.help)

    def help(self):
        display_message(self.aid.localname, "I want to buy a phone, I need your help.")
        message = ACLMessage()
        message.set_performative(ACLMessage.PROPOSE)
        message.add_receiver(AID(name="seller@localhost:8011"))
        self.send(message)

    def send_info(self):
        knowledge = self.knowledge[self.timesAsked]
        self.timesAsked = self.timesAsked + 1
        display_message(self.aid.localname, "{}.".format(knowledge))
        message = ACLMessage()
        message.set_performative(ACLMessage.QUERY_REF)
        message.set_content(json.dumps({'knowledge': knowledge}))
        message.add_receiver(AID(name="seller@localhost:8011"))
        self.send(message)

    def react(self, message):
        super(Customer, self).react(message)
        if message.performative == ACLMessage.NOT_UNDERSTOOD:
            self.send_info()
        if (message.performative == ACLMessage.PROPOSE and self.knowledge2 <= 50000):
            display_message(self.aid.localname, "Thanks,I'll buy it. ")
        if (message.performative == ACLMessage.PROPOSE and self.knowledge2 > 50000):
            display_message(self.aid.localname, "Thanks for the offer but It's too expensive for me.")

class Seller(Agent):
    def __init__(self, aid):
        super(Seller, self).__init__(aid=aid, debug=False)
        self.knownsmartphone = smartphone
        self.knownCost = costs
        self.knownKnowledges = [];

    def get_knowledge2(self):
        num = random.randint(0,len(smartphone)-1)
        self.knowledge2 = cost[num][0]

    def on_start(self):
        super().on_start()

    def questions(self):
        display_message(self.aid.localname, "What Iphone model do you like?" if len(self.knownKnowledges) == 0 else "How much memory do you need?")
        message = ACLMessage()
        message.set_performative(ACLMessage.NOT_UNDERSTOOD)
        message.add_receiver(AID(name="customer@localhost:8022"))
        self.send(message)

    def completing_a_purchase(self,idx):
        display_message(self.aid.localname, "Yes We have this model in stock {}.".format(self.knownsmartpone[idx][0]))
        display_message(self.aid.localname, "Cost of this model is {}".format(self.knownCost[idx][0]))
        message = ACLMessage()
        message.set_performative(ACLMessage.PROPOSE)
        message.set_content(json.dumps({'costs': self.knownCost[idx][0]}))
        message.add_receiver(AID(name="customer@localhost:8022"))
        self.send(message)

    def Facts(self):
        informations = []
        for i in range(len(self.knownKnowledges)):
            informations.append([])
            for j in range(len(self.knownsmartphone)):
                for k in range(len(self.knownsmartphone[j])):
                    if(self.knownsmartphone[j][k] == self.knownKnowledges[i]):
                        informations[i].append(j)
        if(len(informations) == 1 and len(informations[0]) != 1):
            self.questions()
            return
        elif(len(informations) == 1 and len(informations[0]) == 1):
            self.completing_a_purchase(informations[0][0])
            return
        list1 = informations[0]
        for i in range(len(informations)-1):
            list1 = list(set(list1).intersection(informations[i+1]))
        if(len(list1) > 1):
            self.questions()
            return
        elif(len(list1) < 1):
            self.send_refuse()
        else:
            self.completing_a_purchase(list1[0])
            return

    def react(self, message):
        super(Seller, self).react(message)
        if message.performative == ACLMessage.PROPOSE:
            display_message(self.aid.localname, "Let's see.")
            self.questions()
        elif message.performative == ACLMessage.QUERY_REF:
            content = json.loads(message.content)
            knowledge = str(content['knowledge'])
            self.knownKnowledges.append(knowledge)
            self.Facts()

if __name__ == '__main__':

    agents = list()

    seller = Seller(AID(name='seller@localhost:8011'))
    customer = Customer(AID(name='customer@localhost:8022'))

    agents.append(seller)
    agents.append(customer)

    start_loop(agents)
    
#Пример работы программы (так должно работать)                                                                                     
#[customer]  I want to buy a Iphone, I need your help..
#[seller]   Let's see
#[seller]   What Iphone model do you like?
#[customer] Iphone 8.
#[seller] How much memory do you need?
#[customer]   64 gb.
#[seller]  Yes, we have this model in stock.
#[seller] Cost of this model is 35990
#[customer]  Thanks,I'll buy it.
