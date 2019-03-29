import luigi
import logging

logger = logging.getLogger( __name__ )



class LoggingTask( luigi.Task ):

    def __init__( self, *args, **kwargs ):

        super().__init__( *args, **kwargs )

        logger.debug( "(((__init__))) debug" )
        logger.info( "(((__init__))) info" )
        logger.warning( "(((__init__))) warning" )
        logger.error( "(((__init__))) error" )
        logger.critical( "(((__init__))) critical" )


    def run(self):

        logger.debug( "(((run))) debug" )
        logger.info( "(((run))) info" )
        logger.warning( "(((run))) warning" )
        logger.error( "(((run))) error" )
        logger.critical( f"(((run))) critical {__name__}" )
