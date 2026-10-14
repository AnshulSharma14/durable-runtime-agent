#include<iostream>
#include<vector>
#include<string>
struct CountTask{
std::string level;
};
struct CountResult{
 int count{0};
};
int main(int argc,char*argv[]){
    if(argc!=3)
    {
       std::cerr<<"usage : dar count <INFO|WARN|ERROR>"<<std::endl;
       return 1;
    }
    std::string command{argv[1]};
    if(command=="count")
    {   
        std::string label{argv[2]};
        if(label!="INFO"&&label!="ERROR"&&label!="WARN")
        {
           std::cerr<<"unsupported level"<<std::endl;
           return 1;
         }
        CountTask task{label};
        std::vector<std::string>log={"INFO","ERROR","WARN","ERROR","ERROR"};
        CountResult result{0};
        for(const auto & i :log){
        if(i==task.level)
           result.count+=1;
        }
        std::cout<<"count="<<result.count<<std::endl;
    }
    else{
    std::cerr<<"unsupported command"<<std::endl;
    return 1;
    }
    return 0;
}
