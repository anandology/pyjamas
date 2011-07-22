debug_options={}
speed_options={}
pythonic_options={}

all_compile_options = dict(
    internal_ast = False,
    debug = False,
    print_statements=True,
    function_argument_checking=False,
    attribute_checking=False,
    getattr_support=True,
    bound_methods=True,
    descriptors=False,
    source_tracking=False,
    line_tracking=False,
    store_source=False,
    inline_code=False,
    operator_funcs=True,
    number_classes=False,
    create_locals=False,
    stupid_mode=False,
    translator='proto',
)

def add_compile_options(parser):
    global debug_options, speed_options, pythonic_options

    parser.add_option("--internal-ast",
                      dest="internal_ast",
                      action="store_true",
                      help="Use internal AST parser instead of standard python one"
                     )
    parser.add_option("--no-internal-ast",
                      dest="internal_ast",
                      action="store_false",
                      help="Use internal AST parser instead of standard python one"
                     )    

    parser.add_option("--debug-wrap",
                      dest="debug",
                      action="store_true",
                      help="Wrap function calls with javascript debug code",
                     )
    parser.add_option("--no-debug-wrap",
                      dest="debug",
                      action="store_false",
                     )
    debug_options['debug'] = True
    speed_options['debug'] = False

    parser.add_option("--no-print-statements",
                      dest="print_statements",
                      action="store_false",
                      help="Remove all print statements",
                     )
    parser.add_option("--print-statements",
                      dest="print_statements",
                      action="store_true",
                      help="Generate code for print statements",
                     )
    speed_options['print_statements'] = False

    parser.add_option("--no-function-argument-checking",
                      dest = "function_argument_checking",
                      action="store_false",
                      help = "Do not generate code for function argument checking",
                     )
    parser.add_option("--function-argument-checking",
                      dest = "function_argument_checking",
                      action="store_true",
                      help = "Generate code for function argument checking",
                     )
    speed_options['function_argument_checking'] = False
    pythonic_options['function_argument_checking'] = True

    parser.add_option("--no-attribute-checking",
                      dest = "attribute_checking",
                      action="store_false",
                      help = "Do not generate code for attribute checking",
                     )
    parser.add_option("--attribute-checking",
                      dest = "attribute_checking",
                      action="store_true",
                      help = "Generate code for attribute checking",
                     )
    speed_options['attribute_checking'] = False
    pythonic_options['attribute_checking'] = True

    parser.add_option("--no-getattr-support",
                      dest = "getattr_support",
                      action="store_false",
                      help = "Do not support __getattr__()",
                     )
    parser.add_option("--getattr-support",
                      dest = "getattr_support",
                      action="store_true",
                      help = "Support __getattr__()",
                     )
    speed_options['getattr_support'] = False
    pythonic_options['getattr_support'] = True

    parser.add_option("--no-bound-methods",
                      dest = "bound_methods",
                      action="store_false",
                      help = "Do not generate code for binding methods",
                     )
    parser.add_option("--bound-methods",
                      dest = "bound_methods",
                      action="store_true",
                      help = "Generate code for binding methods",
                     )
    speed_options['bound_methods'] = False
    pythonic_options['bound_methods'] = True

    parser.add_option("--no-descriptors",
                      dest = "descriptors",
                      action="store_false",
                      help = "Do not generate code for descriptor calling",
                     )
    parser.add_option("--descriptors",
                      dest = "descriptors",
                      action="store_true",
                      help = "Generate code for descriptor calling",
                     )
    speed_options['descriptors'] = False
    pythonic_options['descriptors'] = True

    parser.add_option("--no-source-tracking",
                      dest = "source_tracking",
                      action="store_false",
                      help = "Do not generate code for source tracking",
                     )
    parser.add_option("--source-tracking",
                      dest = "source_tracking",
                      action="store_true",
                      help = "Generate code for source tracking",
                     )
    debug_options['source_tracking'] = True
    speed_options['source_tracking'] = False
    pythonic_options['source_tracking'] = True

    parser.add_option("--no-line-tracking",
                      dest = "line_tracking",
                      action="store_true",
                      help = "Do not generate code for source tracking on every line",
                     )
    parser.add_option("--line-tracking",
                      dest = "line_tracking",
                      action="store_true",
                      help = "Generate code for source tracking on every line",
                     )
    debug_options['line_tracking'] = True
    pythonic_options['line_tracking'] = True

    parser.add_option("--no-store-source",
                      dest = "store_source",
                      action="store_false",
                      help = "Do not store python code in javascript",
                     )
    parser.add_option("--store-source",
                      dest = "store_source",
                      action="store_true",
                      help = "Store python code in javascript",
                     )
    debug_options['store_source'] = True
    pythonic_options['store_source'] = True

    parser.add_option("--no-inline-code",
                      dest = "inline_code",
                      action="store_false",
                      help = "Do not generate inline code for bool/eq/len",
                     )
    parser.add_option("--inline-code",
                      dest = "inline_code",
                      action="store_true",
                      help = "Generate inline code for bool/eq/len",
                     )
    speed_options['inline_code'] = True

    parser.add_option("--no-operator-funcs",
                      dest = "operator_funcs",
                      action="store_false",
                      help = "Do not generate function calls for operators",
                     )
    parser.add_option("--operator-funcs",
                      dest = "operator_funcs",
                      action="store_true",
                      help = "Generate function calls for operators",
                     )
    speed_options['operator_funcs'] = False
    pythonic_options['operator_funcs'] = True

    parser.add_option("--no-number-classes",
                      dest = "number_classes",
                      action="store_false",
                      help = "Do not use number classes",
                     )
    parser.add_option("--number-classes",
                      dest = "number_classes",
                      action="store_true",
                      help = "Use classes for numbers (float, int, long)",
                     )
    speed_options['number_classes'] = False
    pythonic_options['number_classes'] = True
    
    parser.add_option("--create-locals",
                      dest = "create_locals",
                      action="store_true",
                      help = "Create locals",
                     )

    parser.add_option("--no-stupid-mode",
                      dest = "stupid_mode",
                      action="store_false",
                      help = "Doesn't rely on javascriptisms",
                     )
    parser.add_option("--stupid-mode",
                      dest = "stupid_mode",
                      action="store_true",
                      help = "Creates minimalist code, relying on javascript",
                     )

    parser.add_option("--translator",
                      dest = "translator",
                      default="proto",
                      help = "Specify the translator: proto|dict",
                     )

    def set_multiple(option, opt_str, value, parser, **kwargs):
        for k in kwargs.keys():
            setattr(parser.values, k, kwargs[k])

    parser.add_option("-d", "--debug",
                      action="callback",
                      callback = set_multiple,
                      callback_kwargs = debug_options,
                      help="Set all debugging options",
                     )
    parser.add_option("-O",
                      action="callback",
                      callback = set_multiple,
                      callback_kwargs = speed_options,
                      help="Set all options that maximize speed",
                     )
    parser.add_option("--strict",
                      action="callback",
                      callback = set_multiple,
                      callback_kwargs = pythonic_options,
                      help="Set all options that mimic standard python behavior",
                     )
    parser.set_defaults(**all_compile_options)
    
def get_compile_options(opts):
    d = {}
    for opt in all_compile_options:
        d[opt] = getattr(opts, opt)
    return d
