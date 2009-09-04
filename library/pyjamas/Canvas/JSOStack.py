"""
* Copyright 2008 Google Inc.
*
* Licensed under the Apache License, Version 2.0 (the "License"); you may not
* use this file except in compliance with the License. You may obtain a copy of
* the License at
*
* http:#www.apache.org/licenses/LICENSE-2.0
*
* Unless required by applicable law or agreed to in writing, software
* distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
* WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
* License for the specific language governing permissions and limitations under
* the License.
"""




"""*
* JSO Overlay for an array. Treated as a Stack.
*
* @param <T>
"""
class JSOStack:
    
    """
    * Pre-initialized JSOStack to be used for transient string concatenations
    * without having to instantiate a object. JavaScript is single threaded
    * so we don't have to worry about races.
    """
    
    def __new__(self):
        JS("""
        return [];
        """)
    
    def __init__(self):
        self.scratch = self.__new__()


    def clear(self):
        JS("""
        this.length = 0;
        this._minX = this._minY = this._maxX = this._maxY = null;
        """)


    def getMaxCoordX(self):
        JS("""
        return this._maxX;
        """)


    def getMaxCoordY(self):
        JS("""
        return this._maxY;
        """)


    def getMinCoordX(self):
        JS("""
        return this._minX;
        """)


    def getMinCoordY(self):
        JS("""
        return this._minY;
        """)



    def join(self):
        JS("""
        return this.join("");
        """)


    def logCoordX(self,coordX):
        JS("""
        if (!this._minX) {
            this._minX = coordX;
            this._maxX = coordX;
        } else {
            if (this._minX > coordX) {
                this._minX = coordX;
            } else {
                if (this._maxX < coordX) {
                    this._maxX = coordX;
                }
            }
        }
        """)


    def logCoordY(self,coordY):
        JS("""
        if (!this._minY) {
            this._minY = coordY;
            this._maxY = coordY;
        } else {
            if (this._minY > coordY) {
                this._minY = coordY;
            } else {
                if (this._maxY < coordY) {
                    this._maxY = coordY;
                }
            }
        }
        """)


    def pop(self):
        JS("""
        return this.pop();
        """)


    """
    * For backwards compatibility with IE5 and because this is marginally faster
    * than push() in IE6.
    """
    def append(self,pathStr):
        JS("""
        this[this.length] = pathStr;
        """)


    def __len__(self):
        JS("""
        return this.length;
        """)


