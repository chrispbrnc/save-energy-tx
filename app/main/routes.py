'''
Main Routes

These are the general routes for site
'''
from datetime import datetime
from flask import render_template, flash, redirect, url_for
from app.main import bp
from app.main.forms import MoreInfoForm
from app.main.email import send_moreinfo_email


@bp.route('/', methods=['GET', 'POST'])
@bp.route('/index', methods=['GET', 'POST'])
def index():
    form = MoreInfoForm()

    if form.validate_on_submit():
        send_moreinfo_email(form.email.data)
        flash('Success! Check your inbox for more information.')
        return redirect(url_for('main.index'))

    return render_template('general/index.html', title='Home', form=form)

@bp.route('/faq', methods=['GET'])
def faq():
    items = [
        {
            'title': 'How does Save Energy TX work?',
            'description': "Save Energy TX takes your own home's usage information to find the cheapest plan for you. Our algorithm will calculate costs for each plan on the market. Save Energy TX will discuss the plan and your potential savings leaving you to decided if you want us to switch you over. THEN YOU START SAVING!",
        },
        {
            'title': 'Is it really only $10 a month?',
            'description': "Yes! Other opions on the market will charge you while searching for a plan, take 3-4 months, and give you minimal savings, Save Energy TX will never charge you until you have signed on to a new plan we have suggested. At that point you will be charged $10/month for the duration of the electric contract.",
        },
        {
            'title': 'How long of a contract are you typically signing?',
            'description': "Save Energy TX finds that the best deals are usually in the 6-12 month range, but of course we do find some shorter and longer. We will always be tranparent telling you exactly what length your contract is and when your contract is expiring.",
        },
        {
            'title': 'What if my current contract has a penalty for early cancellation?',
            'description': "We will discuss your options and if paying the fee exceeds your savings we will never recommend you to change. A representative will contact you when your contract is about to expire and hopefully you will consider us then!",
        },
        {
            'title': 'How much will I save?',
            'description': "It depends on your current bill, but it is not uncommon for your bill to be cut in half!",
        },
        {
            'title': 'How do I pay?',
            'description': "We set up a user panel where you can see all of your information and pay manually, but to make things easier we recommend setting up autopay to avoid havign to re-enter your information each time we change contracts.",
        },
    ]
    return render_template('general/faq.html', title='FAQ', items=items)

@bp.route('/contact', methods=['GET', 'POST'])
def contact():
    return render_template('general/contact.html', title='Contact Us')
