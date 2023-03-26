sub = input().upper()
string = input().upper()
status = "Tidak Ketemu"
for i in range(len(string)-len(sub)+1):
    if(string[i:i+len(sub)] == sub):
        status = "Ketemu"
        break
print(status)

# kompleksitas = O(n)

# code by : gonstealyoman
