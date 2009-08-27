""" Copyright 2007,2008,2009 John C. Gunther
* Copyright (C) 2009 Luke Kenneth Casson Leighton <lkcl@lkcl.net>
*
* Licensed under the Apache License, Version 2.0 (the
* "License"); you may not use this file except in compliance
* with the License. You may obtain a copy of the License at:
*
*  http:#www.apache.org/licenses/LICENSE-2.0
*
* Unless required by applicable law or agreed to in writing,
* software distributed under the License is distributed on an
* "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
* either express or implied. See the License for the specific
* language governing permissions and limitations under the
* License.
"""





"""*
*
* Translates parameter names into plain text or HTML snippets that
* represent that parameter's value at a given, "hovered over", point.
* <p>
*
* By passing an instance of a <tt>HoverParameterInterpreter</tt> to
* GChart's <tt>setHoverParameterInterpreter</tt> method, you can teach
* GChart how to expand custom parameters embedded in hovertext
* templates (c.f. <tt>setHovertextTemplate</tt>) in a manner analogous
* to how it expands the built-in parameters <tt>${x}</tt>,
* <tt>$(y)</tt>, and <tt>${pieSliceSize}</tt>.  <p>
*
* <small>
* <i>Note:</i> You can also use a hover parameter interpreter to
* override the built-in parameters, giving them a different meaning,
* numeric format, etc., if you like.
* </small>
* <p>
*
* The Chart Gallery chart below uses a custom hover parameter
* interpreter that allows hover text to include the number (positional
* index) of the curve that contains the hovered over point: <p>
*
* {@code.sample
* ..\..\..\..\..\..\gcharttestapp\src\com\googlecode\gchart\gcharttestapp\client\GChartExample17.java}
*
* <p>
*
* Now, whenever the user hovers over a point on any curve, the curve
* index, along with x,y coordinates, appears in the hover text. Here's
* what the chart looks like when the user hovers over the last point
* of the first curve:<p>
*
* <img
* src="{@docRoot}/com/googlecode/gchart/client/doc-files/gchartexample17.png">
*
* <p>
* Note how, once defined, <tt>${curveNumber}</tt> can be used in a
* manner very similar to how the built-in parameters work. Some
* applications may even allow end-users to edit/generate hover
* template HTML that displays just the information they are
* interested in.
* <p>
*
* If you're looking for something that provides a more convincing
* case for using a <tt>HoverParameterInterpreter</tt>,
* see
* <a
* href="package-summary.html#GChartExample17a">this more realistically
* complex example</a>.
* <p>
*
* <i>Tip:</i> An easy way to format numeric custom parameters is via the
* <tt>formatAsTickLabel</tt> method, since tick label formats are
* often appropriate for numeric hovertext values, too. Note that
* the built-in hover parameters (<tt>${x}</tt>, <tt>${y}</tt>, etc.) use this approach.
* <p>
*
* <i>Tip:</i> If you need more control over the hover feedback than can
* be provided by expanding parameter names embedded in an HTML template
* string, consider using a <tt>HoverUpdateable</tt> widget. You can
* also use both techniques together by invoking
* <tt>hoveredOverPoint.getHovertext</tt>
* from within your hover widget's <tt>hoverUpdate</tt> method.
*
* @see GChart.Symbol#setHovertextTemplate setHovertextTemplate
* @see GChart.Curve.Point#getHovertext getHovertext
* @see GChart.Axis#formatAsTickLabel formatAsTickLabel
* @see HoverUpdateable HoverUpdateable
* @see GChart#setHoverParameterInterpreter setHoverParameterInterpreter
* @see GChart.Symbol#setBrushHeight setBrushHeight
*
"""
interface HoverParameterInterpreter {
    
    """*
    * Returns the value of the named parameter evaluated at the given
    * "hovered over" point. The string should be a plain text or HTML
    * snippet that will be substituted for any <tt>${</tt>...<tt>}</tt>
    * bracketed occurrences of the parameter in any hovertext template
    * string on any chart that uses this hover parameter interpreter.
    * <p>
    *
    * @param paramName the name of the custom parameter. The name must
    * begin with a letter (<tt>a,b,...z</tt> or <tt>A,B,...Z</tt>), and
    * be followed by a sequences of letters, digits (<tt>0,1,..,9</tt>) or
    * underscores (<tt>_</tt>).
    *
    * @param hoveredOver a reference to the point that the mouse
    *   centered brush is currently touching (hovering over).
    *   GChart will never invoke this method with a <tt>None</tt>
    *   <tt>Point</tt> reference.
    *
    * @return a plain text or HTML snippet representing the value of the
    *   named parameter at the hovered-over point, or <tt>None</tt> if
    *   this parameter interpreter does not recognize the given parameter
    *   name.
    *
    *
    * @see HoverParameterInterpreter HoverParameterInterpreter
    *
    """
    String getHoverParameter(String paramName,
    GChart.Curve.Point hoveredOver)


