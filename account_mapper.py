def suggest_contacts(industry):
    if industry == "Energy":
        return [
            "VP Partnerships",
            "Director Business Development",
            "Procurement Manager",
            "Project Director"
        ]

    if industry == "Mining":
        return [
            "Operations Director",
            "Supply Chain Manager",
            "Project Manager"
        ]

    return [
        "Business Development",
        "Procurement"
    ]
