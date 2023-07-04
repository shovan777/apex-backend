def romanToInt(s: str) -> int:
    map_r_i = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    dec_num = 0
    # prev_val = map_r_i[s[0]]
    # prev_sum = 0;
    # for letter in s:
    #     print(letter)
    #     val = map_r_i[letter]
    #     if val > prev_val:
    #         print('I am subtracting')
    #         dec_num -= 2*prev_val
    #     # print(val)
    #     dec_num += val
    #     prev_val = val
    #     print(dec_num)
    prev_val = 0
    for i in range(len(s) - 1, -1, -1):
        # print(i)
        val = map_r_i[s[i]]
        # print('val', val)
        if val < prev_val:
            dec_num -= val
        else:
            dec_num += val
        prev_val = val
    sum()
    return dec_num


print(romanToInt("MCMXCIV"))

# sol in c
# int romanToInt(string s) {
#         int ans=0;
#         unordered_map <char,int> mp{
#         {'I',1},{'V',5},{'X',10},{'L',50},{'C',100},{'D',500},{'M',1000}};

#     for(int i=0;i<s.size();i++){
#         if(mp[s[i]]<mp[s[i+1]]){
#             //for cases such as IV,CM, XL, etc...
#             ans=ans-mp[s[i]];
#         }
#         else{
#             ans=ans+mp[s[i]];
#         }
#     }
#         return ans;
#     }
