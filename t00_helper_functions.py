class RTData:
    def __init__(self, filename ):
        '''
        '''
        f=h5py.File(filename,'r')
        self.stokesv=f['/AOP/Stokes'][()]
        self.theta=f['/AOP/zen'][()]
        self.phi=f['/AOP/az'][()]

        self.solzen=f['/AOP/solzen'][()]*180/np.pi
        self.aod=f['/parameters/AOD'][()]
        self.pfr=f['/parameters/pfr'][()][:2,:]
        self.pfi=f['/parameters/pfi'][()][:2,:]
        self.pcr=f['/parameters/pcr'][()][:2,:]
        self.pci=f['/parameters/pci'][()][:2,:]
        self.vdv=f['/parameters/vdv'][()]
        self.wndspd=f['/parameters/wndspd'][()]
        self.chla=f['/parameters/chla'][()]


        self.refff=f['/parameters/refff'][()]
        self.reffc=f['/parameters/reffc'][()]
        self.vefff=f['/parameters/vefff'][()]
        self.veffc=f['/parameters/veffc'][()]
        self.mfr=f['/parameters/mfr'][()].flatten()
        self.mfi=f['/parameters/mfi'][()].flatten()
        
    def print_par(self,id1):
        print(r"solzen:%3.2f, wind:%3.2f, aod:%3.2f, chla:%4.4f" %\
              (self.solzen[id1], self.wndspd[id1], self.aod[id1], self.chla[id1]))
    
    
def plot_stokesv(theta, phi, stokesv, outfile):

    theta=theta*180.0/np.pi
    ntheta=len(theta)
    nphi=len(phi)
    rx=np.zeros((ntheta, nphi))
    ry=np.zeros((ntheta, nphi))
    for i in range(ntheta):
        for j in range(nphi):
            rx[i,j]=theta[i]*np.cos(phi[j])#*np.pi/180.0)
            ry[i,j]=theta[i]*np.sin(phi[j])#*np.pi/180.0)
    X=rx
    Y=ry

    #plt.plot(theta)
    #plt.plot(phi)
    #plt.imshow(stokesv[0,:,:])

    fig=plt.figure(figsize=(10,3))
    plt.subplot(241)
    Z=stokesv[0].T
    plt.contourf(X,Y,Z, 20, cmap=plt.cm.jet)
    plt.colorbar()
    plt.title("I")


    plt.subplot(245)
    plt.plot(theta, Z[:,0])
    plt.plot(theta[::-1]*-1, Z[::-1,90])
    plt.xlabel("Viewing zenith angle ($^\circ$)")
        

    plt.subplot(242)
    Z=np.sqrt(stokesv[1]**2+stokesv[2]**2).T
    plt.contourf(X,Y,Z, 20, cmap=plt.cm.jet)
    plt.colorbar()
    plt.title("DoLP")

    plt.subplot(246)
    plt.plot(theta, Z[:,0])
    plt.plot(theta[::-1]*-1, Z[::-1,90])
    plt.xlabel("Viewing zenith angle ($^\circ$)")
    
    plt.subplot(243)
    Z=stokesv[1].T
    plt.contourf(X,Y,Z, 20, cmap=plt.cm.jet)
    plt.colorbar()
    plt.title("Q")

    plt.subplot(247)
    plt.plot(theta, Z[:,0])
    plt.plot(theta[::-1]*-1, Z[::-1,90])
    plt.xlabel("Viewing zenith angle ($^\circ$)")
    
    plt.subplot(244)
    Z=stokesv[2].T
    plt.contourf(X,Y,Z, 20, cmap=plt.cm.jet)
    plt.colorbar()
    plt.title("U")

    plt.subplot(248)
    plt.plot(theta, Z[:,0])
    plt.plot(theta[::-1]*-1, Z[::-1,90])
    plt.xlabel("Viewing zenith angle ($^\circ$)")

    plt.tight_layout()

    plt.show()
    plt.savefig(outfile)