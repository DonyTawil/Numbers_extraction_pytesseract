import re, logging

logging.basicConfig(level=logging.DEBUG,format='%(asctime)s - %(levelname)s - %(message)s')

def extract_num(text):
    numRegex = re.compile(r'[+-]?\s*\d*[.,]*\d+')
    nums = numRegex.findall(text)
    
    for i in range(len(nums)):
        nums[i] = nums[i].replace(" ", "")
        nums[i] = nums[i].replace(",", ".")
        nums[i] = float(nums[i])

    return nums
        
if __name__ == "__main__":        
    a = "yo my num is - 2234.223 and 22,65"
    b = extract_num(a)
    print(b)
     
