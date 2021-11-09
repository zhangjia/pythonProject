'''
Created on Dec 14, 2011
@author: pablocelayes
'''

from out import Arithmetic, ContinuedFractions, RSAvulnerableKeyGenerator
import sys

sys.setrecursionlimit(10000000)


def hack_RSA(e, n):
    '''
    Finds d knowing (e,n)
    applying the Wiener continued fraction attack
    '''
    frac = ContinuedFractions.rational_to_contfrac(e, n)
    convergents = ContinuedFractions.convergents_from_contfrac(frac)

    for (k, d) in convergents:

        # check if d is actually the key
        if k != 0 and (e * d - 1) % k == 0:
            phi = (e * d - 1) // k
            s = n - phi + 1
            # check if the equation x^2 - s*x + n = 0
            # has integer roots
            discr = s * s - 4 * n
            if (discr >= 0):
                t = Arithmetic.is_perfect_square(discr)
                if t != -1 and (s + t) % 2 == 0:
                    print("Hacked!")
                    return d


# TEST functions

def test_hack_RSA():
    print("Testing Wiener Attack")
    times = 5

    while (times > 0):
        e, n, d = RSAvulnerableKeyGenerator.generateKeys(1024)
        print("(e,n) is (", e, ", ", n, ")")
        print("d = ", d)

        hacked_d = hack_RSA(e, n)

        if d == hacked_d:
            print("Hack WORKED!")
        else:
            print("Hack FAILED")

        print("d = ", d, ", hacked_d = ", hacked_d)
        print("-------------------------")
        times -= 1


if __name__ == "__main__":
    # test_is_perfect_square()
    # print("-------------------------")
    n = 13135748152922068851807562259991833526175730777484124023612993851829955443156593171810566108770514215820542984343663846287282386582824043046503748787889589613007129391469246232735543477149929538968188602282461287596233699800185109030346300685879023327539247264141675982725321923319965267452566983753865159969071487636488204871579930383673347045053870063722175608993080162716415486448027532424383724695071801571322005261106334877334047211659397929333555608837107626755393427056320625857002257080722498437768960750360112169740061492146894798308307571752422769821088492368556922971780160003588288119154938395902573141227
    e = 12472643612658556362688127761946639081739344859218714559709965256052431749454548817304848413467042472979918287245463205407261868802360251297270401156355632353781495808009882081279433630964865363142433940032882642884450512435389188371663310332918875493370370678126485453550431880160141317463203769606991758739033821056257388276263873215055545829450351157247182688694880384130007649807631727142268128439032681266998342978959845080161998058458873402929597438304194185927609154133353292494116640984586259361644245928207767098232359227782789358653930183953329941354597878943049060831604918661559869393575572607525778785647
    d = hack_RSA(e,n)
    print(d)