def month(n):
    months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
    return months[n-1] if 1 <= n <= 12 else ""
