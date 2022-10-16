def genConcurrentUser():
    print("Calculate number of concurrent users during peak hour")
    number_of_session_during_peak_hourly = int(input("Input the number of Sessions during peak hour: "))
    print("During the peak hour there are", number_of_session_during_peak_hourly, "users access within one hour.")

    session_length = int(input("Input average session length in second: "))
    print("The average duration that users stay in SUT is", session_length, "seconds")

    number_of_concurrent_user = number_of_session_during_peak_hourly * session_length / 3600
    print(round(number_of_concurrent_user), "Concurrent Users")
    print()

def numSessionInPeakHour():
    print("Calculate number of session during peak hour")
    target_daily_users = int(input("Input number of expect daily active users: "))
    num_session_in_peak_hour = target_daily_users * 0.2
    print("number of Sessions during peak hour:", int(num_session_in_peak_hour))
    print("20% of", target_daily_users, "equal to ", int(num_session_in_peak_hour))
    print()

def transectionPerSecond():
    print("Calculate number of transaction per second")
    cocurrent_user_in_peak_hour = int(input("Input number of concurrent user in peak hour: "))
    num_call_per_user_in_a_session_length = int(input("Input number of call per user in during a session length in Second: "))
    txnPerSec = int(cocurrent_user_in_peak_hour * num_call_per_user_in_a_session_length)
    print("Number of Transaction Per Second is: ", txnPerSec)
    print()

numSessionInPeakHour()
genConcurrentUser()
transectionPerSecond()
