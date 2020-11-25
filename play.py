from textwrap import dedent

class entrance(object):

    def enter(self):
        print(dedent("""You arrive at the store with mask on and ready to grab a cart.  Do you take the one on the left or the right?"""))

        guess = input("left or right> ")
        if guess == "left":
            print(dedent("""you picked a cart with a bad wheel.  
            Add 5 minutes to your shopping experience"""))
            return 'produce'
        elif guess == "right":
            print(dedent("""you picked a cart with no bad wheels; you are on your way"""))
            return 'produce'
        else:
            print(dedent("Silly, you need a cart.  Pick the left or right one"))
            return 'entrance'


class produce(object):

    def enter(self):
        print(dedent("""You have pototoes on the list but you don't know how many pounds you need.
        You text Brielle but aren't getting a response.  How many pounds do you grab?"""))

        guess = int(input("> "))
        if guess < 3:
            print(dedent("""It looks like Brielle just texted.  She said that's not enough
            Go back and get some more and add 5 more minutes to shopping"""))
            return 'produce'
        elif guess > 7:
            print(dedent("""It looks like Brielle just texted.  She said that could feed all of Cambridge.  
            Go back and put them back and add 5 more minutes to shopping"""))
            return 'produce'
        elif guess <= 7 or guess >=3:
            print(dedent("""It looks like Brielle just texted.  She said that should be enough.  """))
            return 'turkey'
        else:
            print(dedent("Uh oh. That wasn't an integer"))
            return 'produce'

class turkey(object):

    def enter(self):
        print(dedent("""You've gotten to the turkeys.  
        How do you proceed to get through the crowds: 
        input "one" to say excuse me mam and sir to make a path
        input "two" to be a shy midwesterner and even let others go ahead of you
        input "three" to push in like it's the T to grab your bird"""))
        
        guess = input("one, two or three> ")
        
        if guess == "one":
            print(dedent("""Somebody beat to your turkey, but grabbed another one and didn't lose time"""))
            return 'dessert'
        elif guess == "two":
            print(dedent("""The couple ahead of you throught you were so nice, 
            that they gave you their turkey, but it cost you 10 extra minutes"""))
            return 'dessert'
        elif guess == "three":
            print(dedent("""Uh oh, somebody saw how mean you are and your cart got stolen.  Go back to carts and add 20 minutes"""))
            return 'entrance'
        else:
            print(dedent("Uh oh. That wasn't a choice"))


class dessert(object):

    def enter(self):
        print(dedent("""You need to pick up desserts, but you didn't grab
        a fresh pie when you walked in.  You are right by the frozen pies.  
        Do you go back to the get a fresh on or buy a frozen one?"""))
        
        guess = input("fresh or frozen> ")    
        if guess == "fresh":
            print(dedent("""You snake your way through the aisle and it only took a minute"""))
            return 'finished'
        elif guess == "frozen":
            print(dedent("""You picked up a pie but then you remembered that you should
            have bought a fresh turkey rather than a frozen one.  Add 20 minutes"""))
            return 'turkey'
        else:
            print(dedent("Uh oh. That wasn't a choice"))
            return 'dessert'

class finished(object):

    def enter(self):
        print("you made it through shopping.  Now go home and make the bird")

class Shopping(object):

    def __init__(self,scene_map):
        self.scene_map = scene_map

    def play(self):
        #from other class, define opening scene
        current_scene = self.scene_map.opening_scene()
        #from other class, define last scene using next scene
        last_scene = self.scene_map.next_scene('finished')

        while current_scene != last_scene:
            #if not on last scene, find next scene by going through current scene
            next_scene_name = current_scene.enter()
            #return the next scene from the current one that you are in
            current_scene = self.scene_map.next_scene(next_scene_name)
        
        #this brings you to finished and out of while statement
        current_scene.enter()

class Store(object):
    scenes = {'entrance': entrance(), 'produce': produce(),'turkey': turkey(),"dessert": dessert(),"finished": finished()}

    def __init__(self,start_scene):
        self.start_scene = start_scene
    
    #get function based scene name in dictionary
    def next_scene(self, scene_name):
        val = Store.scenes.get(scene_name)
        return val
    
    #needed for start of game; this will pass through the next scene function to get name of function
    def opening_scene(self):
        return self.next_scene(self.start_scene)


a_map = Store('entrance')
a_game = Shopping(a_map)
a_game.play()



