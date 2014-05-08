import System.Environment
import System.IO  
import Control.Monad
import InversionCounter


convert_list :: [String] -> [Int]
convert_list = map read
getLines = liftM lines . readFile


main = do  
        (filepath:args) <- getArgs
        list <- getLines filepath
        let list' = convert_list list in
          let (sorted_list, count) = inversion_count list' (length list') in
            print count
