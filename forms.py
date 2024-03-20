from flask_wtf import FlaskForm
from wtforms import SelectField

class TestForm(FlaskForm):
    CHOICES = [('0', 'Strongly Disagree'),
               ('1', 'Disagree'),
               ('2', 'Slightly Disagree'),
               ('3', 'Neither Agree nor Disagree'),
               ('4', 'Slightly Agree'),
               ('5', 'Agree'),
               ('6', 'Strongly Agree')]

    ques = [
        'I put effort into work because it has personal significance to me.',
        'I care about having a great reputation at work.',
        'I care about having challenges that help me to develop new skills.',
        'I like to complete tasks way in advance to feel comfortable.',
        'I am motivated by recognition at work.',
        'Its important to me to work in an environment where no one day is the same.',
        'Its important to me to keep up to date with the newest research of my field.',
        'It is important that I am able to take on different kinds of tasks at work.',
        'I want to support others in their learning.',
        'Being publicly praised for my work would feel uncomfortable for me.'
    ]

    Q1 = SelectField(label=ques[0], choices=CHOICES)
    Q2 = SelectField(label=ques[1], choices=CHOICES)
    Q3 = SelectField(label=ques[2], choices=CHOICES)
    Q4 = SelectField(label=ques[3], choices=CHOICES)
    Q5 = SelectField(label=ques[4], choices=CHOICES)
    Q6 = SelectField(label=ques[5], choices=CHOICES)
    Q7 = SelectField(label=ques[6], choices=CHOICES)
    Q8 = SelectField(label=ques[7], choices=CHOICES)
    Q9 = SelectField(label=ques[8], choices=CHOICES)
    Q10 = SelectField(label=ques[9], choices=CHOICES)
