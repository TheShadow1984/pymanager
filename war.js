Mod.event("declareWar", {
    type: "action",
    ui: true,
    category: "diplomacy",

    subject: {
        reg: "player", id: 1
    },

    target: {
        reg: "town"
    },

    check: (subject, target) => {
        return subject.townId !== target.id && !target.war;
    },

    func: (subject, target) => {
        target.war = true;
        target.relation = (target.relation ?? 0) - 100;

        happen("WarDeclared", subject, target, {
            aggressor: subject.townId,
            defender: target.id
        });
    },

    message: (s, t) => `Krieg gegen {{regname:town|${t.id}}} erklären`,

    weight: $c.RARE
});
