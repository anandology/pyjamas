import GChartTestAppUtil
from pyjamas.chart.GChart import GChart
from pyjamas.chart import SymbolType

symbolTypes = [\
    SymbolType.BOX_CENTER,
    SymbolType.BOX_EAST,
    SymbolType.BOX_NORTH,
    SymbolType.BOX_NORTHEAST,
    SymbolType.BOX_NORTHWEST,
    SymbolType.BOX_SOUTH,
    SymbolType.BOX_SOUTHEAST,
    SymbolType.BOX_SOUTHWEST,
    SymbolType.BOX_WEST,
    SymbolType.HBAR_EAST,
    SymbolType.HBAR_NORTHEAST,
    SymbolType.HBAR_NORTHWEST,
    SymbolType.HBAR_SOUTHEAST,
    SymbolType.BOX_SOUTHWEST,
    SymbolType.HBAR_WEST,
    SymbolType.HBAR_NEXT,
    SymbolType.HBAR_PREV,
    SymbolType.NONE,
    SymbolType.VBAR_NORTH,
    SymbolType.VBAR_NORTHEAST,
    SymbolType.VBAR_NORTHWEST,
    SymbolType.VBAR_SOUTH,
    SymbolType.VBAR_SOUTHEAST,
    SymbolType.VBAR_SOUTHWEST,
    SymbolType.VBAR_NEXT,
    SymbolType.VBAR_PREV,
    SymbolType.XGRIDLINE,
    SymbolType.Y2GRIDLINE,
    SymbolType.YGRIDLINE
]
symbolNames = [ \
    "BOX_CENTER",
    "BOX_EAST",
    "BOX_NORTH",
    "BOX_NORTHEAST",
    "BOX_NORTHWEST",
    "BOX_SOUTH",
    "BOX_SOUTHEAST",
    "BOX_SOUTHWEST",
    "BOX_WEST",
    "HBAR_EAST",
    "HBAR_NORTHEAST",
    "HBAR_NORTHWEST",
    "HBAR_SOUTHEAST",
    "BOX_SOUTHWEST",
    "HBAR_WEST",
    "HBAR_NEXT",
    "HBAR_PREV",
    "NONE",
    "VBAR_NORTH",
    "VBAR_NORTHEAST",
    "VBAR_NORTHWEST",
    "VBAR_SOUTH",
    "VBAR_SOUTHEAST",
    "VBAR_SOUTHWEST",
    "VBAR_NEXT",
    "VBAR_PREV",
    "XGRIDLINE",
    "Y2GRIDLINE",
    "YGRIDLINE"
]

"""* Simple chart that uses every possible symbol type."""
class TestGChart02 (GChart):
    def __init__(self):
        GChart.__init__(self, XChartSize=400,YChartSize=400) # bit bigger so 29 curve legend fits
        self.setChartTitle(GChartTestAppUtil.getTitle(self))
        self.setChartFootnotes("Check: Rendering consistent with SymbolType on legend.")
        for i in range(len(symbolTypes)):
            self.addCurve()
            self.getCurve(i).addPoint(i, i)
            self.getCurve(i).getSymbol().setSymbolType(symbolTypes[i])
            self.getCurve(i).getSymbol().setHeight(7)
            self.getCurve(i).getSymbol().setWidth(7)
            self.getCurve(i).setLegendLabel("%d %s " % (i, symbolNames[i]))
        
        self.setLegendFontSize(8)
        self.getXAxis().setTickLabelFontSize(8)
        self.getXAxis().setHasGridlines(True)
        self.getXAxis().setTickCount(len(symbolTypes))
        self.getYAxis().setTickLabelFontSize(8)
        self.getYAxis().setHasGridlines(True)
        self.getYAxis().setTickCount(len(symbolTypes))
        
    


