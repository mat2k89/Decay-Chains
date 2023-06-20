# Extensions

This notebooks contains several possible extensions to the activities we've seen so far which should allow you to extend or modify your code. You should be able to undertake any of them in any order. These activities do not have assocaited tests, so you may want to create your own to make sure your code works as intended.

## Activity 3A - Faster and Faster

Your code works, but can you make it go faster? In research, when solving problems in research some simulations can be very extensive and take a long time to run. Can you identify the operations your code performs which are slow? How much faster can you make your code run?

## Activity 3B - More Decay Modes

So far we've looked at alpha decay, beta decay and electron capture. However, there are many more decay modes possible. You can find a list of decay modes in the section "List of Decay Modes" [here](https://en.wikipedia.org/wiki/Radioactive_decay). Note that some of these decay modes will be difficult to implement. 

For isntance, spontaneous fission is when a nucleus splits through fission, which will cause the creation of a different pair of duaghter isomers each time (along with a nubmer of neutrons). This process would require more data to model than you have access to. As a result, don't worry if you can't model all decay modes.

## Activity 3C - Splitting Chains

Some isomers will have multiple decay modes. For instance, Cf $^{245}$ will decay via electron capture 64% of the time, and alpha decay 36% of time. can you adapt your code so it can model this splitting of the decay chain?

Note that, particularly for the more exotic isomers, the data for the splitting may contain some uncertainty as the isomers are difficult to  produce and study. For instance ```dec-102_No_259.end``` reports a decay mode of ```A=75.00%, EC=25.00%, SF LT 10.00% ```, meaning the isomer decays by alpha decay apporximately 75% of the time, electron capture approximately 25% of the time and spontaneous fission less than 10% of the time. Your code will either have to have a way to either approximate these uncertainties, or ignore the isomer.

## Activity 3D - Power and Energy

As each isomer decays it will release energy. This energy may be carried away in a nubmer of different particles released in the decay. These particles or radiation may be in addition to the main decay mode particle.

The endf dataset has this data for many (but not all) isomers in the section labelled ```Energy Balance```. The power released through each of these types of particles from the decay of Isomer $X$ may be written as:

$$
P_{Xi}(t) = N_{X}(t)N_{A}\chi_{Xi}\lambda_{X},
$$

where $P_{Xi}(t)$ is the power released from Isomer $X$ through the release of particle $i$, $N_{X}(t)$ is the number of moles of Isomer $X$ at time $t$, $N_{A}$ is Avogadro's Constant, $\chi_{Xi}$ is the energy released in particle $i$ when a nucleus of Isomer $X$ decays (this may be found from the endf files), and $\lambda_{X}$ is the decay rate of Isomer $X$.

Adapt your code so it can output the power released from the system in each particle as a function of time. For instance, your code should be able to say what power is released in Gamma rays, alpha particles, neutrinos, etc as a function of time.
