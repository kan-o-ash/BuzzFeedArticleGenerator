import sys
from controller import Controller 

mycontroller = Controller()

def author():
    if len(sys.argv) != 5:
        return 'Usage: {0} num_reddit_posts minimum_entries_in_article keyword_certainty_of_post' .format(sys.argv[0])

    num_to_look_at = int(sys.argv[1])
    min_entries_in_article = int(sys.argv[2])
    certainty_threshold = int(sys.argv[3])
    frequency = sys.argv[4]

    if num_to_look_at < 0 or num_to_look_at > 100:
        return 'Argument 1: Keep the amount of reddit posts looked at between 0 and 100'
    if  min_entries_in_article < 1 or min_entries_in_article > 30:
        return 'Argument 2: Keep the number of articles in an acceptable article between 0 and 30'
    if certainty_threshold < 0 or certainty_threshold > 100:
        return 'Argument 3: The certainty threshold must be between 0 and 100'
    if frequency == 'daily':
        mycontroller.daily_run(num_to_look_at, min_entries_in_article, certainty_threshold/100.00)
    elif frequency == 'weekly':
        mycontroller.weekly_run(num_to_look_at, min_entries_in_article, certainty_threshold/100.00)
    elif frequency == 'monthly':
        mycontroller.monthly_run(num_to_look_at, min_entries_in_article, certainty_threshold/100.00)
    else:
         return 'Argument 4: Frequency must be one of (daily, weekly or monthly)'
return 'Success'
result = author()
print result
