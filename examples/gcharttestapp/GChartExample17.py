from pyjamas.chart import GChartUtil
from pyjamas.chart.GChart import GChart

class CurveNumberHoverParameterInterpreter:

    def getHoverParameter(self, paramName, hoveredOver):

        # Returning None tells GChart "I don't know how to expand that
        # parameter name". The built-in parameters (${x}, ${y}, etc.) won't
        # be processed correctly unless you return None for this "no
        # matching parameter" case.
        result = None
        if "curveNumber" == paramName:
            # The parent of a point is the curve containing it, and the
            # parent of that curve is the GChart itself. So, from the
            # single hovered over point ref., we can self.get at any info
            # within the GChart we may need to generate our snippets.
            result = str(hoveredOver.getParent().getParent().getCurveIndex(
                                    hoveredOver.getParent()))

        # add "elif" branches to support more parameter names

        print "getHoverParam", paramName, hoveredOver, result
        return result

"""*
* Illustrates how to use a <tt>HoverParameterInterpreter</tt> to define
* your own custom parameter names that GChart will then expand when
* included in a hover text template via <tt>setHovertextTemplate</tt>.
* <p>
*
* This example adds a custom parameter called <tt>curveNumber</tt> that
* expands into the index of the curve containing the hovered over
* point.
*
*
"""
class GChartExample17 (GChart):
    def __init__(self):
        GChart.__init__(self)

        self.setChartSize(200, 200)
        self.setBorderWidth("0px")
        self.setHoverParameterInterpreter(
                            CurveNumberHoverParameterInterpreter())
        template = GChartUtil.formatAsHovertext(
                            "Curve #${curveNumber}:<br>x=${x}, y=${y}")
        for iCurve in range(3):
            self.addCurve()
            self.getCurve().getSymbol().setHovertextTemplate(template)
            for iPoint in range(10):
                self.getCurve().addPoint(iPoint, (iCurve+1)*iPoint)



