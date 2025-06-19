public class App {
    static String[] trees = {
            "(7654321,(1,(110,(1110,None,None),(1111,None,None)),(101,(1010,None,None),(1011,None,None))),None)",
            "",
            "(1,None, None )",
            "(1, (2, none, none ), None )",
            "(1, None, (2, none, none ) )",
            "(1, (3, none, none), (2, none, none ) )",
            "(1, (3, (4,none,none), none), (2, none, (5, none,none) ) )",
            "(1, (3, (4,(6,none, (9,none,none)),none), none), (2, none, (5, none,(7, none, none)) ) )",
            "(1,(2,(3,(4,(5,(6,None, None ), None ), None ), None ), None ), None )",
            "(1, None, (2, None, (3, none, (4,none,(5,none,(6,none,(7,          none,(8,none,none)))))) ) )",
            "(   0,          (           1,                (   110,                     (                   1110,                  None,                  None             ),                   (                   1111,                 None,                  None             )              ),                (               101,                     (                 1010,                  None,                  None              ),                   (                 1011,                  None  ,                  None             )              )        ),      None )",
            "(  0,     (  1,       (  110, \t     (1110, None, None), \t\t (1111,None, None) \t  ),       (  101, \t     (1010, None, None ), \t\t (1011, None  , None) \t  ) \t),     (  2,       (  20, \t     (  200, \t\t    (  2000, \t\t       (  20000,  \t\t\t      None, \t\t\t\t  None \t\t\t   ),  \t\t\t   None \t\t    ),  \t\t    None \t\t ),  \t\t None \t  ), \t  (  3,  \t     None,  \t\t None \t  )    )  )",
    };

    public static void main(String[] args) {
        for (String tree : trees) {
            try {
                System.out.println('«' + tree + '»');
                Tree3 newTree = new Tree3(tree);
                int height = Tree3.TreeHeight(newTree);
                System.out.println(String.format("\tTree height: %d", height));
                System.out.println("------------------------------------------");
            } catch (Exception e) {
                System.out.println("vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv");
                System.out.println("Exception: ");
                e.printStackTrace();
                System.out.println("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^");
            } catch (Error e) {
                System.out.println("vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv");
                System.out.println("ERROR: ");
                e.printStackTrace();
                System.out.println("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^");
            }
        }
    }

}
