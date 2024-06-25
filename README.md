# Toller-Prize
Code for my toller prize project. Overall goal is to prove the practical capability and scalability of the deferred admissions algorithm (Gale & Shapley, 1962).

# What The Code Does
*data.py* : Generates a list of n applicants and their preferences of the 20 universities listed in the 'unis' list. These preferences are not random, but rather based on three publicly available rankings of the universities. The average rank is then shifted by a random amount (based on a normal distribution with mean = 0, s.d. = 2. This produces applicant preferences which vary while retaining general similarity (i.e. Oxford will be in the top 5 >95% of the time). A similar approach is used for the preferences of applicants for the universities. These are generally aligned but again vary based on some normally distributed random shifting factor. Returns these two 2D (n x m or vice versa) lists of preferences.

*shapley.py* : Applies Shapley's delayed acceptance algorithm to a dataset of n applicants' preferences and m universities' preferences, given these data and the quotas for each university. Returns optimal, stable assignment in the form of a 2D list.

*checks.py* : Checks for stability in a given assignment given also the original preference lists. Returns True or False.

*main.py* : Uses other files to generate n applicants over 20 universities, apply Shapely's algorithm using realistic quotas for the universities (data in 'quotas' taken from Wikipedia) and check for stability.


