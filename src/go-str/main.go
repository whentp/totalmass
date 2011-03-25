package main

import (
	"fmt"
	//"os"
	//"flag"
	"io/ioutil"
	"regexp"
	"strings"
)

/*
   cutter = re.compile(r"""[a-z0-9\\-|']+""", re.I|re.U|re.M)
   spliter = re.compile(r"""\.|!|\?|;""", re.I|re.U|re.M)
   stripnumber_re = re.compile(r"""[0-9]+(\.[0-9]+)?""", re.I|re.U|re.M)
 */

//func LoadFromFile(filename) [][]string{

func main(){
	cutter,_ := regexp.Compile("[a-z0-9\\-|']+")
	spliter := re.compile(r"""\.|!|\?|;""", re.I|re.U|re.M)
	body,_:=ioutil.ReadFile("./test_data/xx.txt");

tmpstr := strings.ToLower(string(body));

xx := [][]string{{"a","a","a","a"}, {"a","a","a","a"}, {"a","a","a","a"}}
ccc := reg.FindAll([]byte(tmpstr), len(body))
     fmt.Println(len(ccc));
     for _, cccc := range xx{
	     for _, ccccc := range cccc{
		     fmt.Println(string(ccccc))
	     }
	     fmt.Println("\n")
     }

     fmt.Println(string(body[:5000]));

     for _, num:= range [5]int{1,2,3,4,5}{
	     fmt.Println(num);
     }
     fmt.Println("hi.")
     //var a []int

}
