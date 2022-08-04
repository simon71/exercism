import statistics

def get_rounds(number):
    """

     :param number: int - current round number.
     :return: list - current round and the two that follow.
    """
    list = [number]
    list.append(number+1)
    list.append(number+2)
    return list

def concatenate_rounds(rounds_1, rounds_2):
    """

    :param rounds_1: list - first rounds played.
    :param rounds_2: list - second set of rounds played.
    :return: list - all rounds played.
    """
    
    for i in rounds_2: rounds_1.append(i)
    return rounds_1

def list_contains_round(rounds, number):
    """

    :param rounds: list - rounds played.
    :param number: int - round number.
    :return:  bool - was the round played?
    """
    
    if (len(rounds) >= 1 and number >= 1):
        if (number in rounds): 
            return True
        else:
            return False
    else:
        return False
    

def card_average(hand):
    """

    :param hand: list - cards in hand.
    :return:  float - average value of the cards in the hand.
    """
    sum = 0
    for i in hand: sum=sum+i
    size_of_hand = len(hand)
    return float(sum/size_of_hand)


def approx_average_is_average(hand):
    """

    :param hand: list - cards in hand.
    :return: bool - is approximate average the same as true average?
    """
    avg=card_average(hand)
    median=statistics.median(hand)
    first_last_avg=(hand[0]+hand[-1])/2
    return avg==median or avg==first_last_avg

def average_even_is_average_odd(hand):
    """

    :param hand: list - cards in hand.
    :return: bool - are even and odd averages equal?
    """
    even_sum=0
    odd_sum=0
    even_count=0
    odd_count=0

    for i in range(len(hand)):
        if (i%2==0):
            even_sum=even_sum+hand[i]
            even_count=even_count+1
        else:
            odd_sum=odd_sum+hand[i]
            odd_count=odd_count+1
            
    even_avg=even_sum/even_count
    odd_avg=odd_sum/odd_count

    if even_avg==odd_avg: 
        return True
    else:
        return False


def maybe_double_last(hand):
    """

    :param hand: list - cards in hand.
    :return: list - hand with Jacks (if present) value doubled.
    """
    new_hand=[]
    
    for i in hand:
        if i==11:
            new_hand.append(22)
        else:
            new_hand.append(i)

    return new_hand
