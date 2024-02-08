import pandas

student_dict = {
  "student": ["Angela", "James", "Lily"],
  "score": [56, 78, 98]
}

student_df = pandas.DataFrame(student_dict)
print(student_dict)

# # Loop through a data frame
# for (key, value) in student_df.items():
#   print(value)

# Loop through rows of a data frame
for (index, row) in student_df.iterrows():
  if row.student == "Lily":
    print(row.score)