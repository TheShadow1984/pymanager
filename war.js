// Button Event: Krieg erklären zwischen Städten
Mod.event("declareWar", {
    button: true,
    subject: {
        reg: "player", id: 1
    },
    target: {
        reg: "town", random: true
    },

    check: (subject, target) => {
        // optional: verhindert Krieg gegen eigene Stadt oder bereits im Krieg befindliche Ziele
        return subject.townId !== target.id && !target.war;
    },

    func: (subject, target, args) => {
        // setzt Kriegszustand
        target.war = true;

        // optional: Beziehung verschlechtern
        target.relation = (target.relation ?? 0) - 100;

        // optional: Trigger eines Events im Spielsystem
        happen("WarDeclared", subject, target, {
            aggressor: subject.townId,
            defender: target.id
        });
    },

    message: (subject, target, args) =>
        `Krieg gegen {{regname:town|${target.id}}} erklären?`,

    messageDone: (subject, target, args) =>
        `Krieg gegen {{regname:town|${target.id}}} wurde erklärt.`,

    messageNo: (subject, target, args) =>
        `Krieg gegen {{regname:town|${target.id}}} kann nicht erklärt werden.`,

    weight: $c.RARE
});
