class Solution {
public:
    int maxProfit(vector<int>& prices) {
        if (prices.size() < 2) return 0;
        
        bool bought = false;
        int profit = 0;
        
        for(int i = 0; i < prices.size(); i++){
            if (i == prices.size()-1 ) {
                if (bought )   {
                    profit += prices[i];
                    return profit;
                }
                return profit;
            }
                
            if (prices[i] < prices[i+1] && !bought) {
                profit -= prices[i];
                bought = true;
            }
               
            if (prices[i] > prices[i+1] && bought) {
                profit += prices[i];
                bought = false;
            }    
                
              
        }
        return profit;
    }   
};