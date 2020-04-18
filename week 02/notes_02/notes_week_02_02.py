start1 = int(input())
end1 = int(input())
start2 = int(input())
end2 = int(input())
# is_s1_in2 = start2 <= start1 <= end2
# is_e1_in2 = start2 <= end1 <= end2
# is_s2_in1 = start1 <= start2 <= end1
# is_e2_in1 = start1 <= end2 <= end1
# answer = is_s1_in2 or is_e1_in2 or is_s2_in1 or is_e2_in1
answer = start1 <= end2 and start2 <= end1
print(answer)
