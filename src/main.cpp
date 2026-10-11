#include<iostream>
#include<vector>
#include<string>
int main(){
    std::vector<std::string>log={"INFO","ERROR","WARN","ERROR","ERROR"};
    int count{0};
    for(const auto & i :log){
       if(i=="ERROR")
           count+=1;
	}
    std::cout<<"error_count="<<count<<std::endl;
    return 0;
}
