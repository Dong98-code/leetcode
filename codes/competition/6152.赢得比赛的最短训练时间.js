var minNumberOfHours = function(initialEnergy, initialExperience, energy, experience) {
    let res = 0;
    let n = energy.length;
    for (let i = 0;i<n;i++) {
        if (initialEnergy > energy[i] && initialExperience > experience[i]) {
            initialEnergy -= energy[i];
            initialExperience += experience[i];
        } else {
            if (initialEnergy <= energy[i]) {
                res += energy[i]+1 - initialEnergy;
                initialEnergy = 1;
            }
            if (initialExperience <= experience[i]) {
                res += experience[i] + 1 - initialExperience;
                initialExperience = experience[i]+1;
            }
        }
    }
    return res;
};
console.log(minNumberOfHours(5,3,[1,4,3,2],[2,6,3,1]))