
function ajiletestload ()
{
    /*Ajile.EnableCloak(false);*/
    /*Ajile.EnableDebug();*/
    /*Ajile.EnableOverride(false);*/

    /*Namespace("other");*/
    
    Import("other.test");

    other.test.Fred();
/*
    test.me.NewModule = new function()
    {
        alert("NewModule");
        other.test.Fred();
    }

    test.me.NewModule();
    */
}

