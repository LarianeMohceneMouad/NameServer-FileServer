def helper_msg_stripper(sm):
    helper_auth = sm[0:6]
    state = sm[6:]
    return helper_auth, state


msg = "HELPERF1F2"
print(helper_msg_stripper(msg))