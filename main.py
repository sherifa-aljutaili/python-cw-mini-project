#PT1
def padel_court_cost (court_type):
    if court_type == 'indoor' :
        return 30 
    elif court_type == 'outdoor' :
        return 20
    else :
        return False


#PT2
def rakets_cost (raket_brand) :
    if raket_brand == 'bullpadel' :
        return 100
    elif raket_brand == 'nox' :
        return 140
    elif raket_brand == 'siux' :
        return 200
    else :
        return False


#PT3
def padel_balls_cost (ball_boxes) :
     if ball_boxes == 1 :
         return 2
     elif ball_boxes == 2 :
         return 3.5
     elif ball_boxes == 3 :
         return 5
     else :
         return False
  
     
#PT4
def padel_game_cost () :
    court_type = input("what type of courts you whant to play in ? , ENTER : indoor, outdoor......")
    raket_brand = input("what raket brand you want to use ? , ENTER : bullpadel, nox, siux......")
    ball_boxes = int(input("How many box of balls you want ? , ENTER : 1, 2, 3......"))
    print( padel_court_cost (court_type) + rakets_cost (raket_brand) + padel_balls_cost (ball_boxes) )

padel_game_cost()
