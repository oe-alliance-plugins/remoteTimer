from setuptools import setup
import setup_translate

pkg = 'Extensions.remoteTimer'
setup(name='enigma2-plugin-extensions-remotetimer',
       version='3.0',
       description='add Timer remote on a another Dreambox with Enigma2',
       package_dir={pkg: 'remoteTimer'},
       packages=[pkg],
       package_data={pkg: ['images/*.png', '*.png', '*.xml', 'locale/*/LC_MESSAGES/*.mo', '*.info']},
       cmdclass=setup_translate.cmdclass,  # for translation
      )
