number_of_session_during_peak_hourly = int(input("Input the number of Sessions during peak hour: "))
print("During the peak hour there are", number_of_session_during_peak_hourly, "users access within one hour.")

session_length = int(input("Input average session length in second: "))
print("The average duration that users stay in SUT is", session_length, "seconds")

number_of_concurrent_user = number_of_session_during_peak_hourly * session_length / 3600
print(round(number_of_concurrent_user), "Concurrent Users")