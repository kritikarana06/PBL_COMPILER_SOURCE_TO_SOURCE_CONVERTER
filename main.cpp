#include <iostream>
#include "codegen.h"
#include "node.h"

#define YY_STDINIT

using namespace std;

extern int yyparse();
extern NBlock *programBlock;

int main(int argc, char **argv)
{
    std::cerr << "[INFO] Starting parser" << std::endl;

    if (argc >= 2)
    {
        freopen(argv[1], "r", stdin);
        std::cerr << "[INFO] Reading from file: " << argv[1] << std::endl;
    }
    else
    {
        freopen("input.c", "r", stdin);
        std::cerr << "[INFO] Reading from file: in.c" << std::endl;
    }

    freopen("out.py", "w", stdout);
    std::cerr << "[INFO] Writing to file: out.py" << std::endl;

    yyparse();
    std::cerr << "[INFO] Finished parsing" << std::endl;
    std::cerr << programBlock << std::endl;

    CodeGenContext context;
    context.generateCode(*programBlock);
    std::cerr << "[INFO] Finished generating code" << std::endl;

    if (context.errorMessage.size() != 0)
    {
        std::cerr << "[ERROR] Compilation failed" << std::endl;
        for (auto msg : context.errorMessage)
        {
            std::cerr << msg << std::endl;
        }
        return 2;
    }

    std::cerr << "[INFO] Compilation successful" << std::endl;
    std::string code = context.outputCode();
    std::cout << code << std::endl;

    return 0;
}
