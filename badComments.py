#!/bin/python

# Do whatever you want with it license
# Ascii art is from http://www.chris.com/ascii/index.php
# Some of the art was modified slightly to allow it to be embedded
# inspired by the comments here - http://www.reddit.com/r/compsci/comments/1bgrio/maintenance_coders_of_reddit_what_are_some_of_the/
import sys
import os
import random
import time
import string


numBlankLines = 100
blankSpace = range(numBlankLines)

comments = [
r"""
// What do you expect to find here? And if you find what you seek, will you truly be happy?
%s
//Thar be dragons here!
%s


                                              ,....,. 
                                          ..''   .' 
                                       .'"       | 
                                    .''          \ 
                                 .''              \. 
                               .'                  ."., 
                             ,:'             ..,'"'   '...,..::/""..... 
                           /'"          .,'"'  .,',:,'""'         .,'' 
                         ,'.'      .,'"' ..,''' ""         .'   ."' 
                       ,'  \, ..,''  .,''. ..,'""        ./   ." 
                     ."     .,"  .,'".,"'./           ..''   / 
                    ,'    .'  ./'.,"'  .'  "'     ." '.     / 
                  .'   ./' ./"."\,..,''     '" ../,     ,  | 
                 ,   ./' .'./'|/     ............        ',| 
                /   /' ,'.".,'""\..... '""''''''  .::/'.., | 
               /  ." ,' ':\ ""''  |  ,      ''          '""   \ 
              /  /'.''. |:::::::""' ,' ' ''. ".,.,  ""'    .""' 
             | ." /.,":. ""..,   "\'.."'..  ;"'  '\.'""' ." \
             | \.:\.    '""./\ \  | ' '" .,"".           / 
             / \'   '"..     ", \  \,',     "'..  .,     ' 
            /.'",''..,  '\,   '\ ". '\'.,     , "'. "'.,| 
           .,'        '". ',    \ '.".. ''../'      "" __\ 
           '             \,',    \  '.'\..,  ","'  .'" 
                         |  |    '| ,\""'\/.  |  ." 
            ."          .|  .    / / ./'. '.".' /' 
            /'        ..|':""''\././  /   "  '/\.' 
           //  ./  .'"    /' ./'.' .'  | ..,  ':| 
         ./:  ,/   |",   ' ."'  :  '   |    .../:, 
        .'.'.\/   /.'           ''  .,   ..\' 
      .,\.\".'   /"    ,"' \...,      "\.\| ", 
     /    ./""''   ..:    ',|  "".,     '\  ', 
  .,' "'   \|     "".'".    '/  .| '\.     ", '\ 
 /          \.    ../,   "./ '\ |'  \/"" '".'\  \ 
/   '\\:.   \,"\::'  ./""'    ./|  .'     .'"/| '| 
' ,"\:"/""''  /'  ."\'  .., |:| .| |'    .'' .\|  ', 
|/  / /'    .'| /  |. \,    /'"/. |  |:\..," .||  \ 
'' /.'      //\|'  '\/\:.   :,/"'::.  ,   ..::'|  | 
            ||'/,    '\\/"\ '/|    '\ '"::::"| || . 
            || \\       "".   ...,  '.  \\...| |' | 
            ||  "\,         .".\, ". ', | \  '||  | 
             '              |\|'|\/.''\ | |\  ||  | 
                            ||\/"/| '\, ., / / /  , 
                             ' \  "   '"  / / .' / 
                                '      .'".' .' / 
       -hrr-                      ..'"'.." ." ." 
                              .,"":.'""..'" ." 
                         .,:'"'"'  .'"  ..'" 
                       ." ."'..'""...,"' 
                    .." "    , ""' 
                   /  . :/"' 
                 .'  :/' 
                /  /' 
               / .' 
              / ' 
             /.' 
             ' 
%s
"""%("\n"*random.choice(blankSpace), "\n"*random.choice(blankSpace),"\n"*random.choice(blankSpace)), 

r'''
      __            /^\
    .'  \          / :.\   
   /     \         | :: \ 
  /   /.  \       / ::: | 
 |    |::. \     / :::'/  
 |   / \::. |   / :::'/
 `--`   \'  `~~~ ':'/`
         /         (    
        /   0 _ 0   \   
      \/     \_/     \/  
    -== '.'   |   '.' ==-   
      /\    '-^-'    /\    
        \   _   _   /             
       .-`-((\o/))-`-.   
  _   /     //^\\     \   _    
."o".(    , .:::. ,    )."o".  
|o  o\\    \:::::/    //o  o| 
 \    \\   |:::::|   //    /   
  \    \\__/:::::\__//    /   
   \ .:.\  `':::'`  /.:. /      
    \':: |_       _| ::'/  
 jgs `---` `"""""` `---`
 ''',

r'''

                                                  `T",.`-, 
                                                     '8, :. 
                                              `""`oooob."T,. 
                                            ,-`".)O;8:doob.'-. 
                                     ,..`'.'' -dP()d8O8Yo8:,..`, 
                                   -o8b-     ,..)doOO8:':o; `Y8.`, 
                                  ,..bo.,.....)OOO888o' :oO.  ".  `-. 
                                , "`"d....88OOOOO8O88o  :O8o;.    ;;,b 
                               ,dOOOOO""""""""O88888o:  :O88Oo.;:o888d 
                               ""888Ob...,-- :o88O88o:. :o'"""""""Y8OP 
                               d8888.....,.. :o8OO888:: :: 
                              "" .dOO8bo`'',,;O88O:O8o: ::, 
                                 ,dd8".  ,-)do8O8o:"""; ::: 
                                 ,db(.  T)8P:8o:::::    ::: 
                                 -"",`(;O"KdOo::        ::: 
                                   ,K,'".doo:::'        :o: 
                                    .doo:::"""::  :.    'o: 
        ,..            .;ooooooo..o:"""""     ::;. ::;.  'o. 
   ,, "'    ` ..   .d;o:"""'                  ::o:;::o::  :; 
   d,         , ..ooo::;                      ::oo:;::o"'.:o 
  ,d'.       :OOOOO8Oo::" '.. .               ::o8Ooo:;  ;o: 
  'P"   ;  ;.OPd8888O8::;. 'oOoo:.;..         ;:O88Ooo:' O"' 
  ,8:   o::oO` 88888OOo:::  o8O8Oo:::;;     ,;:oO88OOo;  ' 
 ,YP  ,::;:O:  888888o::::  :8888Ooo::::::::::oo888888o;. , 
 ',d: :;;O;:   :888888::o;  :8888888Ooooooooooo88888888Oo; , 
 dPY:  :o8O     YO8888O:O:;  O8888888888OOOO888"" Y8o:O88o; , 
,' O:  'ob`      "8888888Oo;;o8888888888888'"'     `8OO:.`OOb . 
'  Y:  ,:o:       `8O88888OOoo"""""""""""'           `OOob`Y8b` 
   ::  ';o:        `8O88o:oOoP                        `8Oo `YO. 
   `:   Oo:         `888O::oP                          88O  :OY 
    :o; 8oP         :888o::P                           do:  8O: 
   ,ooO:8O'       ,d8888o:O'                          dOo   ;:. 
   ;O8odo'        88888O:o'                          do::  oo.: 
  d"`)8O'         "YO88Oo'                          "8O:   o8b' 
 ''-'`"            d:O8oK  -hrr-                   dOOo'  :o": 
                   O:8o:b.                        :88o:   `8:, 
                   `8O:;7b,.                       `"8'     Y: 
                    `YO;`8b' 
                     `Oo; 8:. 
                      `OP"8.` 
                       :  Y8P 
                       `o  `, 
                        Y8bod. 
                        `""""' 
''',

r'''
 *      _    _
 *     / \__/ \_____
 *    /  /  \  \    `\
 *    )  \''/  (     |\
 *    `\__)/__/'_\  / `
 *       //_|_|~|_|_|
 *       ^""'"' ""'"' ''', 

 '''To future maintainers: get out now.''',

'''It's %f O'clock'''%time.time(),

'''Database secret key: %s''' %''.join([random.choice(string.digits+string.letters+string.punctuation) for _ in range(32)])

 ]

multiLineComments = {".py":"'''\n%s\n'''", 
					 ".c":"/*\n%s\n*/",
					 ".cpp":"/*\n%s\n*/",
					 ".hs":"{-\n%s\n-}",
					 ".pl":"\n=item\n%s\n=cut",
					 ".rb":"=begin\n%s\n=end",
					 ".js":"/*\n%s\n*/",
					 ".html":"<!--\n%s\n-->",
					 }

def comment_poorly(filePath):
	'''
	Input: File to add terrible comments to.
	Outputs: Terribly commented file.
	'''
	try:
		with open(filePath, "rb") as f:
	   		data = f.readlines()
	
		comment = random.choice(comments)
		fileName, fileExtension = os.path.splitext(filePath)
		multilineComment = multiLineComments.get(fileExtension, None)
		if multilineComment:
			commentedLines = multilineComment%comment
			insertionPoint = random.choice(range(len(data)))
			data.insert(insertionPoint, commentedLines)
			with open(filePath, "wb") as f:
				f.write(''.join(data))

	except IOError:
		print 'No file named %s' %filePath

if __name__ == "__main__":
  if len(sys.argv) >= 1:
  	files = sys.argv[1:]
  	for filePath in files:
  		print "Adding bad comments to %s"%filePath
  		comment_poorly(filePath)
