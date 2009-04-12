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
* An in-browser SQL database. Gears provides a SQL database using SQLite
* syntax. For details, see the <a href="http:#www.sqlite.org/lang.html">SQLite
* syntax.</a>
*
* Note that this class (and its related classes) intentionally do NOT implement
* the JDBC interface, since the database provided by Gears does necessarily
* implement all those semantics. It may be possible to add a JDBC layer on top
* of this, but it's unclear whether that would really be useful.
"""

class GearsDatabase:

    def __init__(self, db):

        self.db = db

    def close(self):
        #try:
            self.uncheckedClose()
        #except ex:
        #    raise DatabaseException(ex.getDescription(), ex)
        
    def execute(self, sqlStatement, *args):
        #try:
            if args:
                return self.execute_args(sqlStatement, args)
            else:
                return self.execute_args(sqlStatement)
        #except ex:
        #    raise DatabaseException(ex.getDescription(), ex)

    def getLastInsertRowId(self):
        JS("""
        return this.db.lastInsertRowId;
        """)

    def getRowsAffected(self):
        JS("""
        return this.db.rowsAffected;
        """)

    def open(self, name=None):
        if name is None:
            JS(" this.db.open(); ")
        else:
            JS(" this.db.open(name); ")


    def execute_args(self, sqlStatement, args):
        JS("""
        if (typeof args == 'undefined') {
            return this.db.execute(sqlStatement);
        } else {
            return this.db.execute(sqlStatement, args.l);
        }
        """)


    def uncheckedClose(self):
        JS("""
        this.db.close();
        """)


