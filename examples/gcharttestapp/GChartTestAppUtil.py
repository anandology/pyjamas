import pyjd

"""*
*
* Displays the test  chart in the browser, and checks the HTML
* generated against previous, visually validated, browser
* output HTML hash codes to see if HTML output from the test
* has changed (possibly due to an error).
*
* As long as GChart and the test set itself has not changed,
* these tests can be performed by first running in hosted
* mode, then clicking on the "Compile/Browse" button. If
* "Test passed" is displayed in hosted mode and also in
* Firefox after the compile (this assumes Firefox is your default browser)
* it means that the generated HTML has not changed since
* the last time it was visually inspected--test passed.
*
* If the test or GChart changes so as to change browser output,
* you will have to visually verify the charts, and then (assuming the
* charts are correct) enter the hashcodes.
*
* In the most common case where the test and output are unchanged,
* the test should go through very quickly.
*
"""
    
# convenience method to create a short, class-name-based title
def getTitle(obj):
    result = obj.__class__.__name__
    result = result[:result.rfind(".")+1]
    return "<h4><br>" + result + "</h4>"


""" Linear congruent random number generator.
*
* Cannot use GWT's Math.random() because, for automated
* testing, we require that the exact same random sequence
* be used each time (GWT does not support the JDK's more
* generic Random class, which would have allowed this).
*
* Constants are from Knuth via Numerical Recipes in C.
*
"""
i = 0
def rnd(self):
    m = 217728
    a = 84589
    c = 45989
    i = (a*i + c) % m
    return i/m


